# -*- coding: utf-8 -*-
import os
from ddhi_encoder.ne_extractor import NeExtractor

__author__ = "Clifford Wulfman"
__copyright__ = "Clifford Wulfman"
__license__ = "mit"

test_file = os.path.join(
    os.path.dirname(__file__),
    "standoff_sample.tei.xml"
    )


def test_place_names():
    extractor = NeExtractor(test_file)
    assert b'foo' in extractor.place_names()

