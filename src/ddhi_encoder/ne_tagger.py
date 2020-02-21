# -*- coding: utf-8 -*-
# ne_tagger.py

import spacy
from lxml import etree
from abc import ABC, abstractmethod


class NamedEntityTagger(object):
    def __init__(self):
        self._nlp = False
        self._creators = {}

    @property
    def nlp(self):
        return self._nlp

    @nlp.setter
    def nlp(self, spacy_nlp_object):
        self._nlp = spacy_nlp_object

    def register_named_entity(self, entity_name, creator):
        self._creators[entity_name] = creator

    def is_registered(self, entity_name):
        if self._creators.get(entity_name):
            return True
        else:
            return False

    def named_entity(self, name):
        entity = self._creators.get(name)
        if not entity:
            raise ValueError(name)
        return entity


class DDHINETagger(NamedEntityTagger):
    TEI_NAMESPACE = "http://www.tei-c.org/ns/1.0"
    TEI = "{%s}" % TEI_NAMESPACE
    NSMAP = {None: TEI_NAMESPACE}  # default namespace

    def __init__(self):
        super().__init__()
        self.register_named_entity("PERSON", PERSON)
        self.register_named_entity("GPE", GPE)
        self.register_named_entity("EVENT", EVENT)
        self.register_named_entity("DATE", DATE)

    def tag_element(self, element):
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

        return "".join(textlist)


class NamedEntityTaggerFactory:
    def tagger_for(self, project):
        if project == "DDHI":
            return DDHINETagger()


class NamedEntity(ABC):
    def __init__(self, text):
        self.text = text

    def xml(self):
        element = etree.Element("name")
        element.text = self.text
        return element

    def to_str(self):
        return etree.tostring(self.xml()).decode()

    # def __repr__(self):
    #     return etree.tostring(self.xml()).decode()

    # def __str__(self):
    #     return etree.tostring(self.xml()).decode()


class PERSON(NamedEntity):
    def xml(self):
        element = etree.Element("persName")
        element.text = self.text
        return element


class GPE(NamedEntity):
    def xml(self):
        element = etree.Element("placeName")
        element.text = self.text
        return element


class EVENT(NamedEntity):
    def xml(self):
        element = etree.Element("name", type="event")
        element.text = self.text
        return element


class DATE(NamedEntity):
    def xml(self):
        element = etree.Element("date")
        element.text = self.text
        return element

