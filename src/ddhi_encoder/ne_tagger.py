# -*- coding: utf-8 -*-
# ne_tagger.py

import spacy
from lxml import etree
from abc import ABC, abstractmethod
import pdb


class NamedEntityTagger(object):
    def __init__(self, nlp, element_to_tag):
        self._nlp = nlp
        self._doc = nlp(element_to_tag.text)
        self._root = element_to_tag
        self._creators = set()
        self.current_entity = {}
        self._latest_entity = None
        self._idx = None

    @property
    def nlp(self):
        return self._nlp

    @nlp.setter
    def nlp(self, spacy_nlp_object):
        self._nlp = spacy_nlp_object

    def register_named_entity(self, entity_name):
        self._creators.add(entity_name)

    def is_registered(self, entity_name):
        return entity_name in self._creators

    def in_entity(self):
        return self.current_entity

    def in_registered_entity(self):
        if self.in_entity():
            return self.is_registered(self.current_entity['type'])
        else:
            return False

    def curr_tok(self):
        return self._doc[self._idx]

    def curr_tail(self):
        if list(self._root):
            return list(self._root)[-1]
        else:
            return None

    def append_to_root(self):
        self._root.text = self.curr_tok().text + self.curr_tok().whitespace_

    def append_to_tail(self):
        latest_tail = self.curr_tail().tail
        tok = self.curr_tok()
        self.curr_tail().tail = latest_tail + tok.text + tok.whitespace_

    def append_to_end(self):
        if self._root.getchildren():
            self.append_to_tail()
        else:
            self.append_to_root()

    def update_current_entity(self):
        self.current_entity['type'] = self._doc[self._idx].ent_type_
        self.current_entity['start'] = self._idx

    def process_token(self, idx):
        self._idx = idx
        tok = self._doc[self._idx]
        if tok.ent_iob_ == 'B':
            self.process_B()
        elif tok.ent_iob_ == 'I':
            self.process_I()
        elif tok.ent_iob_ == 'O':
            self.process_O()
        else:
            raise ValueError(tok.ent_iob_)

    def process_B(self):
        if self.current_entity:
            self.process_entity_queue()
        self.update_current_entity()

    def process_I(self):
        pass

    def process_O(self):
        if self.current_entity:
            self.process_entity_queue()
            # self.update_current_entity()
            self.current_entity = {}
        self.append_to_end()

    def named_entity(self, name):
        entity = self._creators.get(name)
        if not entity:
            raise ValueError(name)
        return entity

    def process_entity_queue(self):
        if self.in_registered_entity():
            entity = NamedEntity(self.current_entity['type'])
            entity.element.text = self._doc[self.current_entity['start']:self._idx].text
            # add whitespace_ to tail
            entity.element.tail = self._doc[self._idx].whitespace_
            self._root.append(entity.element)
            self._latest_entity = entity
        else:
            self.append_to_end()

        self.current_entity = {}

    def reset_root(self):
        attrs = self._root.items()
        self._root.clear()
        [self._root.set(k, v) for k, v in attrs]

    def tag(self):
        self.reset_root()
        for idx, tok in enumerate(self._doc):
            self.process_token(idx)
        self.complete()


class DDHINETagger(NamedEntityTagger):
    TEI_NAMESPACE = "http://www.tei-c.org/ns/1.0"
    TEI = "{%s}" % TEI_NAMESPACE
    NSMAP = {None: TEI_NAMESPACE}  # default namespace

    def __init__(self, nlp, element_to_tag):
        super().__init__(nlp, element_to_tag)
        self.register_named_entity("PERSON")
        self.register_named_entity("GPE")
        self.register_named_entity("EVENT")
        self.register_named_entity("DATE")

    def tag_element_wrong(self, element):
        doc = self._nlp(element.text)
        # cache the attributes before clearing the element's contents
        attrs = element.items()
        element.clear()
        [element.set(k, v) for k, v in attrs]
        in_ent = False
        for idx, tok in enumerate(doc):
            if tok.ent_iob_ == 'B':
                in_ent = True
                ent = tok.ent_type_
                start = idx
                continue
            if tok.ent_iob_ == 'I':
                element.append(doc[idx-1].whitespace_)
                continue
            if tok.ent_iob_ == 'O':
                if in_ent:
                    if self.is_registered(ent):
                        entity_factory = self.named_entity(ent)
                        entity = entity_factory(doc[start:idx].text)
                        element.append(entity.xml())
                        element.append(doc[idx-1].whitespace_)
                    else:
                        element.append(doc[start:idx].text)
                        element.append(doc[idx-1].whitespace_)
                in_ent = False
                element.append(doc[idx].text_with_ws)
        if in_ent:
            entity_factory = self.named_entity(ent)
            entity = entity_factory(doc[start:idx].text)
            element.append(entity.xml())
        return element

    def tag_element_old(self, element):
        doc = self._nlp(element.text)
        textlist = []
        in_ent = False
        for idx, tok in enumerate(doc):
            if tok.ent_iob_ == 'B':
                in_ent = True
                ent = tok.ent_type_
                start = idx
                continue
            if tok.ent_iob_ == 'I':
                textlist.append(doc[idx-1].whitespace_)
                continue
            if tok.ent_iob_ == 'O':
                if in_ent:
                    if self.is_registered(ent):
                        element_factory = self.named_entity(ent)
                        element = element_factory(doc[start:idx].text)
                        textlist.append(element.to_str())
                        textlist.append(doc[idx-1].whitespace_)
                    else:
                        textlist.append(doc[start:idx].text)
                        textlist.append(doc[idx-1].whitespace_)
                in_ent = False
                textlist.append(doc[idx].text_with_ws)
        if in_ent:
            element_factory = self.named_entity(ent)
            element = element_factory(doc[start:].text)
            textlist.append(element.to_str())

        return etree.XML("".join(textlist))


class NamedEntityTaggerFactory:
    def tagger_for(self, project):
        if project == "DDHI":
            return DDHINETagger()


class NamedEntity():
    def __init__(self, ename):
        if ename == "PERSON":
            self.element = etree.Element("persName")
        elif ename == "GPE":
            self.element = etree.Element("placeName")
        elif ename == "EVENT":
            self.element = etree.Element("name", type="event")
        elif ename == "DATE":
            self.element = etree.Element("date")
        else:
            raise ValueError(ename)
