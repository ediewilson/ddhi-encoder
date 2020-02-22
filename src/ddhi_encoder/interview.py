# -*- coding: utf-8 -*-
# interview.py
from lxml import etree


class Interview:
    TEI_NAMESPACE = "http://www.tei-c.org/ns/1.0"
    TEI = "{%s}" % TEI_NAMESPACE
    XML_NAMESPACE = "http://www.w3.org/XML/1998/namespace"
    XML = "{%s}" % XML_NAMESPACE
    NSMAP = {None: TEI_NAMESPACE, "xml": XML_NAMESPACE}

    def __init__(self):
        self.namespaces = {"tei": "http://www.tei-c.org/ns/1.0"}

    def read(self, path):
        self.tei_doc = etree.parse(path,
                                   etree.XMLParser(remove_blank_text=True))

    def write(self, path):
        self.tei_doc.write(path,
                           pretty_print=True,
                           encoding='UTF-8')
