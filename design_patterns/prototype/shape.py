import abc
from typing import Optional


class Shape(abc.ABC):
    x: int
    y: int
    color: str

    @abc.abstractmethod
    def __init__(self, source: Optional["Shape"] = None):
        """Can't overload then keep logic in clone method. Or optional"""
        if source:
            self.x = source.x
            self.y = source.y
            # self.color = source.color

    @abc.abstractmethod
    def clone(self) -> "Shape":
        ...


class Rectangle(Shape):
    width: int
    height: int

    def __init__(self, source: Optional["Rectangle"] = None):
        super().__init__(source)
        if source:
            self.width = source.width
            self.height = source.height

    def clone(self) -> "Shape":
        return Rectangle(self)


class Circle(Shape):
    radius: int

    def __init__(self, source: Optional["Circle"] = None):
        super().__init__(source)
        if source:
            self.radius = source.radius

    def clone(self) -> "Shape":
        return Circle(self)

