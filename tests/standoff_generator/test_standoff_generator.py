# -*- coding: utf-8 -*-
import os
from ddhi_encoder.standoff_generator.standoff_generator import StandoffGenerator

test_xml = os.path.join(os.path.dirname(__file__), "test.xml")


def test_generator():
    subject = StandoffGenerator()
    assert type(subject).__name__ == "Generator"
