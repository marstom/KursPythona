from typing_extensions import Protocol


class Graphic(Protocol):
    def move(self, x: int, y: int):
        ...

    def draw(self):
        ...


class Dot(Graphic):
    def __init__(self, x, y):
        self._x = x
        self._y = y
        ...

    def move(self, x: int, y: int):
        print(f"moved dot by {x} {y}")
        self._x += x
        self._y += x

    def draw(self):
        print("Draw dot!")


class Circle(Dot):
    def __init__(self, x, y, radius):
        self._y = y
        self._x = x
        self._radius = radius

    def draw(self):
        print("Draw circle!")


class CompoundGraphic(Graphic):

    def __init__(self):
        self._children: list[Graphic] = []

    def add(self, child: Graphic):
        self._children.append(child)

    def remove(self, child: Graphic):
        if child in self._children:
            self._children.remove(child)

    def move(self, x: int, y: int):
        print(f"moved graphic by {x} {y}")
        for child in self._children:
            child.move(x, y)

    def draw(self):
        for child in self._children:
            child.draw()
