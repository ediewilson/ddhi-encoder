# -*- coding: utf-8 -*-
from lxml import etree
import csv


class Modifier(object):
    def __init__(self, target):
        self._target = target

    @property
    def target(self):
        return self._target

    def modify(self):
        pass


class Standoff(Modifier):
    TEI_NAMESPACE = "http://www.tei-c.org/ns/1.0"
    TEI = "{%s}" % TEI_NAMESPACE
    XML_NAMESPACE = "http://www.w3.org/XML/1998/namespace"
    XML = "{%s}" % XML_NAMESPACE
    NSMAP = {None: TEI_NAMESPACE, "xml": XML_NAMESPACE}

    def __init__(self, target):
        self.namespaces = {"tei": "http://www.tei-c.org/ns/1.0",
                           "xml": "http://www.w3.org/XML/1998/namespace"}
        super().__init__(target)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, filename):
        with open(filename) as file:
            reader = csv.DictReader(file, dialect="excel-tab")
            self._data = []
            for row in reader:
                self._data.append(row.copy())

    def modify(self):
        tei = self.target.tei_doc.xpath("//tei:TEI",
                                        namespaces=self.namespaces)[0]

        standoff = etree.Element(self.TEI + "standoff", nsmap=self.NSMAP)
        tei.append(standoff)
        
