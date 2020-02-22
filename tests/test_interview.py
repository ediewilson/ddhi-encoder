# -*- coding: utf-8 -*-

import os
from lxml import etree
from ddhi_encoder.interview import Interview


__author__ = "Clifford Wulfman"
__copyright__ = "Clifford Wulfman"
__license__ = "mit"

test_file = os.path.join(
    os.path.dirname(__file__),
    "aninterview.xml"
    )


def test_io():
    interview = Interview()
    interview.read(test_file)
    assert b'TEI' in etree.tostring(interview.tei_doc)
    outfile = os.path.join('/tmp', 'test_interview_tmpfile.xml')
    try:
        os.remove(outfile)
    except OSError:
        pass
    interview.write(outfile)
    assert os.path.isfile(outfile)
