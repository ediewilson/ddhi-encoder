# -*- coding: utf-8 -*-

import pytest
import re
from ddhi_encoder.interview import Interview
from ddhi_encoder.word_parser import WordParser
from ddhi_encoder.utterance import Utterance

__author__ = "Clifford Wulfman"
__copyright__ = "Clifford Wulfman"
__license__ = "mit"


def test_interview():
    parser = WordParser()
    interview = Interview(parser, "short.docx")
    assert interview.utterances[1].speaker == ('TAVELA')
    assert re.search('Washington', interview.utterances[1].speech)

def test_utterance():
    speaker = "John"
    speech = "Now is the time"
    utterance = Utterance(speaker, speech)
    assert utterance.speaker == speaker
    assert utterance.speech == speech
    assert len(utterance) == len(speech)
