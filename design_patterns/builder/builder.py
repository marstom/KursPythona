import abc

from engine import Engine
from car import Car, Manual


class Builder(abc.ABC):
    @abc.abstractmethod
    def reset(self):
        ...

    @abc.abstractmethod
    def set_seats(self, n: int):
        ...

    @abc.abstractmethod
    def set_engine(self, engine: Engine):
        ...

    @abc.abstractmethod
    def set_trip_computer(self):
        ...

    @abc.abstractmethod
    def set_gps(self):
        ...


class CarBuilder(Builder):
    __car: Car

    def __init__(self):
        self.reset()

    def reset(self):
        self.__car = Car()

    def set_seats(self, n: int):
        self.__car.seats = n

    def set_engine(self, engine: Engine):
        self.__car.engine = engine

    def set_trip_computer(self):
        self.__car.trip_computer = True

    def set_gps(self):
        self.__car.gps = True

    def get_product(self) -> Car:
        product = self.__car
        self.reset()
        return product



class CarManualBuilder(Builder):
    __manual: Manual
    man_title: str

    def __init__(self, man_title):
        self.man_title = man_title
        self.reset()

    def reset(self):
        self.__manual = Manual(title=self.man_title, pages=[])

    def set_seats(self, n: int):
        self.__manual.pages.append(f"Number of seats is {n}")

    def set_engine(self, engine: Engine):
        self.__manual.pages.append(f"Engine params {engine.hp}")

    def set_trip_computer(self):
        self.__manual.pages.append(f"Has trip computer!")

    def set_gps(self):
        self.__manual.pages.append(f"Has GPS!")

    def get_product(self) -> Manual:
        product = self.__manual
        self.reset()
        return product
