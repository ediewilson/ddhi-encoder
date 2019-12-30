# -*- coding: utf-8 -*-
# word_parser.py

import re
from docx2python import docx2python
from ddhi_encoder.utterance import Utterance

class WordParser:
    def __init__(self):
        self.utt = re.compile(r'^([A-Z]+):\s+(.*?)$')
        self.utterances = []

    def utterance(self, para):
        m = self.utt.match(para)
        if m:
            return Utterance(m.group(1), m.group(2))

    def parse(self, path_to_docx):
        self._extracted = docx2python(path_to_docx)
        self.utterances = list(filter(None,
                                      [ self.utterance(p) for p in self._extracted.body[0][0][0] ]))
        
