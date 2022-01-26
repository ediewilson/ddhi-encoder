# -*- coding: utf-8 -*-
import os
#from ttu_encoder.transformer import Transformer
from ttu_encoder.transformer.transformer import Transformer
from lxml import etree


thunk = os.path.join(os.path.dirname(__file__), 'test.xsl')
test_xml = os.path.join(os.path.dirname(__file__), "test.xml")

def test_xsl():
    subject = Transformer()
    assert type(subject).__name__ == "Transformer"
    output = subject.transform_with_xsl(thunk, test_xml)
    assert "<?xml" in str(output)

