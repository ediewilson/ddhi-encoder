# -*- coding: utf-8 -*-
from lxml import etree
import csv


class Modifier(object):
    TEI_NAMESPACE = "http://www.tei-c.org/ns/1.0"
    TEI = "{%s}" % TEI_NAMESPACE
    XML_NAMESPACE = "http://www.w3.org/XML/1998/namespace"
    XML = "{%s}" % XML_NAMESPACE
    NSMAP = {None: TEI_NAMESPACE, "xml": XML_NAMESPACE}

    def __init__(self, target):
        self.namespaces = {"tei": "http://www.tei-c.org/ns/1.0",
                           "xml": "http://www.w3.org/XML/1998/namespace"}
        self._target = target

    @property
    def target(self):
        return self._target

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
        pass


class Standoff(Modifier):
    def modify(self):
        for row in self.data:
            expr = f"//*[@xml:id = \"{row['id']}\"]"
            place = self.target.tei_doc.xpath(expr)[0]
            placeName = place.xpath('tei:placeName',
                                    namespaces=self.namespaces)
            if len(placeName):
                placeName[0].text = row['placeName']
            else:
                placeName = etree.element(self.TEI + "placeName",
                                          nsmap=self.NSMAP)
                placeName.text = row['placeName']
                place.append(placeName)

            if row['coordinate location']:
                location = etree.SubElement(place, self.TEI + "location",
                                            nsmap=self.NSMAP)
                geo = etree.SubElement(location, self.TEI + "geo",
                                       nsmap=self.NSMAP)
                # TODO: remove comma in the geo text
                geo.text = row['coordinate location'].replace(',', ' ')

            if row['QID']:
                idno = etree.SubElement(place, self.TEI + "idno",
                                        nsmap=self.NSMAP)
                idno.set("type", "WD")
                idno.text = row['QID']


class Event(Modifier):
    def modify(self):
        for row in self.data:
            expr = f"//*[@xml:id = \"{row['id']}\"]"
            event = self.target.tei_doc.xpath(expr)[0]

            desc = event.xpath('tei:desc',
                                    namespaces=self.namespaces)
            if len(desc):
                desc[0].text = row['name']
            else:
                desc = etree.element(self.TEI + "desc",
                                          nsmap=self.NSMAP)
                desc.text = row['name']
                event.append(desc)

            if row['point in time']:
                event.set("when-iso", row['point in time'])

            if row['start time']:
                event.set("from-iso", row['start time'])

            if row['end time']:
                event.set("to-iso", row['end time'])
                          
            if row['QID']:
                idno = etree.SubElement(event, self.TEI + "idno",
                                        nsmap=self.NSMAP)
                idno.set("type", "WD")
                idno.text = row['QID']
