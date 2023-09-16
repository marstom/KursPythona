from math import sqrt


class RoundPeg:
    def __init__(self, radius: int):
        self.__radius = radius

    def get_radius(self) -> int:
        return self.__radius

class RoundHole:

    def __init__(self, radius: int):
        self.__radius = radius

    def get_radius(self) -> int:
        return self.__radius

    def fits(self, peg: RoundPeg) -> bool:
        return self.__radius >= peg.get_radius()



## To adaptee
class SquarePeg:
    def __init__(self, width: int):
        self.__width = width

    def get_width(self) -> int:
        return self.__width


class SquarePegAdapter:
    def __init__(self, peg: SquarePeg):
        self.__peg = peg

    def get_radius(self):
        return self.__peg.get_width() * sqrt(2) / 2