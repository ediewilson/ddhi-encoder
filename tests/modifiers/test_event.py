# -*- coding: utf-8 -*-
from ttu_encoder.modifiers.modifiers import Event
from ttu_encoder.interview import Interview
import os


def test_tsv():
    tsv = os.path.join(os.path.dirname(__file__),
                       "events.tsv")
    iv = os.path.join(os.path.dirname(__file__),
                      "lovely.tei.xml")
    interview = Interview()
    interview.read(iv)
    modifier = Event(interview)
    modifier.data = tsv
    assert modifier.data[0]['name'] == "Vietnam War"
    assert modifier.data[0]['QID'] == "Q8740"


def test_modification():
    tsv = os.path.join(os.path.dirname(__file__),
                       "events.tsv")
    iv = os.path.join(os.path.dirname(__file__),
                      "lovely.tei.xml")
    interview = Interview()
    interview.read(iv)
    events = interview.events()
    assert events[0][0].text == "World War II"
    modifier = Event(interview)
    modifier.data = tsv
    modifier.modify()
    assert events[0][0].text == "Attack on Pearl Harbor"
    assert events[0].get("when-iso") == "1941-12-07T00:00:00Z"
    assert events[0][1].text == 'Q52418'
    assert events[0][1].get("type") == "WD"

    assert events[1][0].text == "Vietnam War"
    assert events[1].get("from-iso") == "1965-11-01T00:00:00Z"
    assert events[1].get("to-iso") == "1975-04-30T00:00:00Z"
