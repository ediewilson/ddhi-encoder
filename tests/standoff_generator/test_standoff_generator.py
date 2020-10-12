# -*- coding: utf-8 -*-
import os
from ddhi_encoder.standoff_generator.standoff_generator import StandoffGenerator

test1_xml = os.path.join(os.path.dirname(__file__), "test1.xml")


def test_generator():
    subject = StandoffGenerator(test1_xml)
    assert type(subject).__name__ == "StandoffGenerator"
