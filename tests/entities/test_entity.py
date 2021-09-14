# -*- coding: utf-8 -*-
from lxml import etree
from ddhi_encoder.entities.entities import Entity,Place

def test_simple():
    entity = etree.ElementTree(
        etree.XML('''\
        <person xmlns="http://www.tei-c.org/ns/1.0" xml:id="foo">
        <persName>Cliff</persName>
        <idno type="WD">Q12345</idno>
        <idno type="DDHI">7890</idno>
        </person>
        '''))

    subject = Entity(entity)
    assert subject.idno['DDHI'] == '7890'
    assert subject.idno['WD'] == 'Q12345'
    assert subject.id == "foo"


def test_place():
    entity = etree.ElementTree(
        etree.XML('''\
       <place xml:id="place1" xmlns="http://www.tei-c.org/ns/1.0">
            <placeName>Hanover, New Hampshire</placeName>
            <location>
               <geo>43.702222 -72.206111</geo>
            </location>
            <desc>The project may wish to provide descriptions of
            entities, if none are available elsewhere; but you will
            gain great extensibility if you can link these entities to
            global authority databases, like WikiData. The idno
            element (with type WD, for WikiData) provides that link.</desc>
            <idno type="WD">Q131908</idno>
         </place>
        '''))
    subject = Place(entity)
    assert subject.idno['WD'] == "Q131908"
    assert subject.coordinates == "43.702222 -72.206111"
    assert subject.description.split()[0:2] == ["The", "project"]
