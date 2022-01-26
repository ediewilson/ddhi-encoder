# -*- coding: utf-8 -*-
from ttu_encoder.modifiers.modifiers import Person
from ttu_encoder.interview import Interview
import os


def test_tsv():
    tsv = os.path.join(os.path.dirname(__file__),
                       "persons.tsv")
    iv = os.path.join(os.path.dirname(__file__),
                      "lovely.tei.xml")
    interview = Interview()
    interview.read(iv)
    modifier = Person(interview)
    modifier.data = tsv
    assert modifier.data[2]['persName'] == "Bernie Sanders"
    assert modifier.data[2]['QID'] == "Q359442"


def test_modification():
    tsv = os.path.join(os.path.dirname(__file__),
                       "persons.tsv")
    iv = os.path.join(os.path.dirname(__file__),
                      "lovely.tei.xml")
    interview = Interview()
    interview.read(iv)
    persons = interview.persons()
    assert persons[2][0].text == "Bernie [presidential candidate Bernard Sanders]"
    modifier = Person(interview)
    modifier.data = tsv
    modifier.modify()
    assert persons[2][0].text == "Bernie Sanders"
    assert persons[2][1].text == "Q359442"
    assert persons[2][1].get("type") == "WD"
