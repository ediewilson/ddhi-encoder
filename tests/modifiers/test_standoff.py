# -*- coding: utf-8 -*-
from ddhi_encoder.modifiers.modifiers import Standoff
from ddhi_encoder.interview import Interview
import os


def test_tsv():
    tsv = os.path.join(os.path.dirname(__file__),
                       "lovely.tsv")
    iv = os.path.join(os.path.dirname(__file__),
                      "lovely.tei.xml")
    interview = Interview()
    interview.read(iv)
    modifier = Standoff(interview)
    modifier.data = tsv
    assert modifier.data[1]['placeName'] == "Boston"
