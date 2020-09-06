# -*- coding: utf-8 -*-
from ddhi_encoder.modifiers.modifiers import Standoff
from ddhi_encoder.interview import Interview
import os
from lxml import etree

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


def test_modification():
    tsv = os.path.join(os.path.dirname(__file__),
                       "lovely.tsv")
    iv = os.path.join(os.path.dirname(__file__),
                      "lovely.tei.xml")
    interview = Interview()
    interview.read(iv)
    places = interview.places()
    assert places[0][0].text == "Rauner [Special Collections] Library"
    modifier = Standoff(interview)
    modifier.data = tsv
    modifier.modify()
    assert places[0][0].text == "Rauner Special Collections Library"

    rauner_loc = "43.70447 -72.28817"
    assert places[0][1][0].text == rauner_loc
