# -*- coding: utf-8 -*-
from ttu_encoder.modifiers.modifiers import Org
from ttu_encoder.interview import Interview
import os


def test_tsv():
    tsv = os.path.join(os.path.dirname(__file__),
                       "test_orgs.tsv")
    iv = os.path.join(os.path.dirname(__file__),
                      "lovely.tei.xml")
    interview = Interview()
    interview.read(iv)
    modifier = Org(interview)
    modifier.data = tsv
    assert modifier.data[0]['orgName'] == "United States Coast Guard"
    assert modifier.data[0]['QID'] == "Q11224"


def test_modification():
    tsv = os.path.join(os.path.dirname(__file__),
                       "test_orgs.tsv")
    iv = os.path.join(os.path.dirname(__file__),
                      "lovely.tei.xml")
    interview = Interview()
    interview.read(iv)
    orgs = interview.orgs()
    assert orgs[0][0].text == "[U.S.] Coast Guard"
    modifier = Org(interview)
    modifier.data = tsv
    modifier.modify()
    assert orgs[0][0].text == "United States Coast Guard"
    assert orgs[0][1].text == "Q11224"
    assert orgs[0][1].get("type") == "WD"
