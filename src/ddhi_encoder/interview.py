# -*- coding: utf-8 -*-
# interview.py

import re
from docx2python import docx2python

def utterance(s):
    utt = re.compile(r'^([A-Z]+):\s+(.*?)$')
    m = utt.match(s)
    if m:
        return ( m.group(1), m.group(2) )
    

class Interview:
    def __init__(self, path_to_docx):
        self.docx = docx2python(path_to_docx)


    def text(self):
        return self.docx.text

    def utterances(self):
        return list(filter(None, [ utterance(p) for p in self.docx.body[0][0][0] ]))
        
        
