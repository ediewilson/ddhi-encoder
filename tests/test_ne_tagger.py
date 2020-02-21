# -*- coding: utf-8 -*-

import pytest
from lxml import etree
import spacy
from ddhi_encoder.ne_tagger import NamedEntityTaggerFactory, DDHINETagger, NamedEntity, PERSON, EVENT, GPE, DATE

__author__ = "Clifford Wulfman"
__copyright__ = "Clifford Wulfman"
__license__ = "mit"


def test_PERSON():
    text = "Martha Washington"
    concern = PERSON(text)
    assert concern.text == text
    xml = concern.xml()
    assert xml.tag == "persName"
    assert xml.text == text


def test_GPE():
    text = "thunk"
    concern = GPE(text)
    assert concern.text == text
    xml = concern.xml()
    assert xml.tag == "placeName"
    assert xml.text == text


def test_EVENT():
    text = "thunk"
    concern = EVENT(text)
    assert concern.text == text
    xml = concern.xml()
    assert xml.tag == "name"
    assert xml.get("type") == "event"
    assert xml.text == text

    # Now test the Named Entity Tagger class


nlp = spacy.load("en_core_web_sm")
utterance = etree.Element("u")
utterance.text = "Jane ate yesterday and burped."


def test_tagger():
    tagger = NamedEntityTaggerFactory().tagger_for("DDHI")
    assert isinstance(tagger, DDHINETagger)
    tagger.nlp = nlp
    result = tagger.tag_element(utterance)
    assert result == "<persName>Jane</persName> ate <date>yesterday</date> and burped."
