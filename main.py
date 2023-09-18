#!/usr/bin/env python3
from abc import ABC
from PrettyPrint import PrettyPrintTree

class Element(ABC):
    def add_child(self, elem):
        elem.owner = self
        self._children.append(elem)

    def get_children(self):
        return self._children

    def __init__(self, elem=None):
        self.owner = None
        self._children = []

        if elem:
            elem.add_child(self)

class RangeElement(Element, ABC):
    pass

class TextBox(Element):
    pass

class TextEdit(TextBox):
    pass

class ScrollBar(RangeElement):
    pass

class SpinBox(RangeElement):
    pass

class Slider(RangeElement):
    pass

class ProgressBar(RangeElement):
    pass

class BaseButton(Element, ABC):
    pass

class Button(BaseButton):
    pass

class TextureButton(BaseButton):
    pass

class CheckBox(BaseButton):
    pass

class ToggleButton(BaseButton):
    pass

class OptionButton(BaseButton):
    pass

class Container(Element, ABC):
    pass

class MarginContainer(Container):
    pass

class CenterContainer(Container):
    pass

class GridContainer(Container):
    pass

class ScrollContainer(Container):
    pass


root = MarginContainer()
g = GridContainer(root)

c = CenterContainer(g)
s = ScrollContainer(g)

t = TextBox(c)

g2 = GridContainer(s)
e = TextEdit(g2)
pb = ProgressBar(g2)
sl = Slider(g2)

g3 = GridContainer(g2)
b1 = Button(g3)
b2 = CheckBox(g3)
b3 = ToggleButton(g3)

pt = PrettyPrintTree(lambda x: x._children, lambda x: type(x).__name__)
pt(root)
