# -*- coding: utf-8 -*-

import pytest
import re
from ddhi_encoder.interview import Interview

__author__ = "Clifford Wulfman"
__copyright__ = "Clifford Wulfman"
__license__ = "mit"


def test_interview():
    interview = Interview("short.docx")
    text = interview.text()
    assert re.search('Rauner', text)
    assert interview.utterances()[1][0] == ('TAVELA')
