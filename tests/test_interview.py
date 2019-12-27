# -*- coding: utf-8 -*-

import pytest
from ddhi_encoder.interview import Interview

__author__ = "Clifford Wulfman"
__copyright__ = "Clifford Wulfman"
__license__ = "mit"


def test_interview():
    interview = Interview("i1")
    assert interview.id == "i1"
