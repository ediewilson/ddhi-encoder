# -*- coding: utf-8 -*-
# interview.py
from lxml import etree


class Interview:
    def __init__(self, parser, path_to_docx, path_to_template, model):
        parser.parse(path_to_docx)
        self.utterances = parser.utterances
        self._model = model
        self.tei_doc = etree.parse(path_to_template)
        self.namespaces = {'tei': 'http://www.tei-c.org/ns/1.0'}

        for utt in self.utterances:
            utt.doc = self._model(utt.speech)

    def update_tei(self):
        body = self.tei_doc.xpath('//tei:body', namespaces=self.namespaces)[0]
        for e in list(body):
            body.remove(e)
        for utt in self.utterances:
            body.append(utt.xml())

    def xml(self):
        return etree.tostring(self.tei_doc, pretty_print=True)
