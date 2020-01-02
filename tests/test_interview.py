# -*- coding: utf-8 -*-

import pytest
import re
from ddhi_encoder.interview import Interview
from ddhi_encoder.word_parser import WordParserFactory
from ddhi_encoder.utterance import Utterance

__author__ = "Clifford Wulfman"
__copyright__ = "Clifford Wulfman"
__license__ = "mit"


def test_interview():
    factory = WordParserFactory()

    parser = factory.parser_for("DDHI")
    interview = Interview(parser, "short.docx")
    assert interview.utterances[1].speaker == ('TAVELA')
    assert re.search('Washington', interview.utterances[1].speech)
