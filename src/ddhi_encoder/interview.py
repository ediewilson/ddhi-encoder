# -*- coding: utf-8 -*-
# interview.py

class Interview:
    def __init__(self, parser, path_to_docx):
        parser.parse(path_to_docx)
        self.utterances = parser.utterances
