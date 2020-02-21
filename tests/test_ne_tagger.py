# -*- coding: utf-8 -*-

import pytest
from lxml import etree
from ddhi_encoder.ne_tagger import NamedEntityTaggerFactory, NamedEntity, PERSON, EVENT, GPE

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
