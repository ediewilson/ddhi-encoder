# -*- coding: utf-8 -*-
# interview.py
import os
from lxml import etree
from abc import ABC, abstractmethod
from ddhi_encoder.word_parser import WordParserFactory
import spacy


class Interview:
    def __init__(self, parser, path_to_docx, path_to_template, model):
        parser.parse(path_to_docx)
        self.utterances = parser.utterances
        self._model = model
        self.tei_doc = etree.parse(path_to_template, etree.XMLParser(remove_blank_text=True))
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

    def to_file(self, filename):
        self.tei_doc.write(filename, pretty_print=True)


class InterviewFactory:
    def interview_for(self, project, path_to_docx):
        if project == "DDHI":
            factory = WordParserFactory()
            template = os.path.join(os.path.dirname(__file__), 'teitemplate.xml')
            parser = factory.parser_for("DDHI")
            model = spacy.load("en_core_web_sm")
            return Interview(parser, path_to_docx, template, model)
