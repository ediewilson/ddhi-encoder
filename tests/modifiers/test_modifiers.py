# -*- coding: utf-8 -*-
from ddhi_encoder.modifiers.modifiers import Modifier


def test_simple():
    class Fooer(Modifier):
        def modify(self):
            self.target.name = "foo"

    class Bar:
        def __init__(self, name):
            self.name = name

    bar = Bar("bar")
    assert bar.name == "bar"
    modifier = Fooer(bar)
    modifier.modify()
    assert bar.name == "foo"
