# -*- coding: utf-8 -*-
from ttu_encoder.modifiers.modifiers import Place
from ttu_encoder.interview import Interview
import os


def test_tsv():
    tsv = os.path.join(os.path.dirname(__file__),
                       "lovely.tsv")
    iv = os.path.join(os.path.dirname(__file__),
                      "lovely.tei.xml")
    interview = Interview()
    interview.read(iv)
    modifier = Place(interview)
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
    modifier = Place(interview)
    modifier.data = tsv
    modifier.modify()
    assert places[0][0].text == "Rauner Special Collections Library"

    rauner_loc = "43.70447 -72.28817"
    assert places[0][1][0].text == rauner_loc

    rauner_qid = "Q98544730"
    assert places[0][2].text == rauner_qid
    assert places[0][2].get("type") == "WD"
