# -*- coding: utf-8 -*-
import os
from ttu_encoder.ne_extractor import NeExtractor

__author__ = "Clifford Wulfman"
__copyright__ = "Clifford Wulfman"
__license__ = "mit"

test_file = os.path.join(
    os.path.dirname(__file__),
    "standoff_sample.tei.xml"
    )


def test_places():
    extractor = NeExtractor(test_file)
    list = extractor.place_names_list()
    assert list[0]['id'] == 'dvp_17_place1'


def test_events():
    extractor = NeExtractor(test_file)
    assert len(extractor.events()) == 7


def test_persons():
    extractor = NeExtractor(test_file)
    assert len(extractor.persons()) == 14


def test_orgs():
    extractor = NeExtractor(test_file)
    assert len(extractor.orgs()) == 21
