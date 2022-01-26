# -*- coding: utf-8 -*-
from ttu_encoder.modifiers.modifiers import Standoff
from ttu_encoder.interview import Interview
from lxml import etree
import os


def test_modification():
    iv = os.path.join(os.path.dirname(__file__),
                      "test_standoff.tei.xml")
    interview = Interview()
    interview.read(iv)
    path = interview.tei_doc.xpath("//tei:standOff/tei:listPlace",
                                   namespaces=interview.namespaces)
    so = interview.standOff()
    assert len(so) == 1
    assert len(path) == 0
    interview.write("/tmp/before.xml")
    modifier = Standoff(interview)
    modifier.modify()
    interview.write("/tmp/after.xml")
    doc = interview.tei_doc
    path = doc.xpath("//tei:standOff/tei:listPlace/tei:place[1]/tei:placeName[1]/text()",
                                   namespaces=interview.namespaces)
    assert path[0] == "Rauner [Special Collections] Library"

    an_event = doc.xpath("//tei:standOff/tei:listEvent/tei:event[1]/tei:desc[1]/text()",
                                   namespaces=interview.namespaces)
    assert an_event[0] == "Vietnam War"

    a_person = doc.xpath("//tei:standOff/tei:listPerson/tei:person[1]/tei:persName[1]/text()",
                         namespaces=interview.namespaces)
    assert a_person[0] == "Emily Burack"

    assert doc.xpath("//tei:standOff/tei:listOrg/tei:org[1]/tei:orgName[1]/text()",
                     namespaces=interview.namespaces)[0] == "Dartmouth College"
