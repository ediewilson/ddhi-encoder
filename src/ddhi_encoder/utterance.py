# -*- coding: utf-8 -*-
# utterance.py

import spacy
from lxml import etree

class Utterance:
    TEI_NAMESPACE = "http://www.tei-c.org/ns/1.0"
    TEI = "{%s}" % TEI_NAMESPACE
    NSMAP = {None: TEI_NAMESPACE}  # default namespace

    def __init__(self, speaker, speech):
        self.speaker = speaker
        self.speech = speech

    def __len__(self):
        return len(self.speech)

    @property
    def nlp(self):
        return self._nlp

    @nlp.setter
    def nlp(self, spacy_nlp_object):
        self._nlp = spacy_nlp_object

    def process(self):
        self._doc = self.nlp(self.speech)

    def xml(self):
        utt_elem = etree.Element(self.TEI + "u", who=self.speaker, nsmap=self.NSMAP)
        utt_elem.text = self.speech
        return etree.tostring(utt_elem)
        
