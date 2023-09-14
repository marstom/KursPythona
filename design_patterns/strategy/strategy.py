import abc
from enum import Enum
from typing import Protocol


class Shipping(abc.ABC):
    @abc.abstractmethod
    def get_cost(self):
        ...

    @abc.abstractmethod
    def get_date(self):
        ...


class Ground(Shipping):
    def __init__(self, line_items, shipping_cost):
        self.shipping_cost: int = shipping_cost
        self.line_items: list = line_items

    def get_cost(self):
        return max(0, len(self.line_items) * self.shipping_cost)

    def get_date(self):
        return "12-12-2022"


class Air(Shipping):
    def __init__(self, line_items, shipping_cost):
        self.shipping_cost: int = shipping_cost
        self.line_items: list = line_items

    def get_cost(self):
        return max(20, len(self.line_items) * self.shipping_cost)

    def get_date(self):
        return "01-01-2022"


class ShType(Enum):
    GROUND = "GROUND"
    AIR = "AIR"


class Order:
    def __init__(self, line_items: list, shipping_cost: int, shipping: Shipping):
        self.shipping = shipping
        self.line_items = line_items
        self.shipping_cost = shipping_cost

    def get_total(self):
        return 100

    def get_shipping_cost(self):
        if self.shipping == ShType.GROUND:
            return max(0, len(self.line_items) * self.shipping_cost)
        if self.shipping == ShType.AIR:
            return max(20, len(self.line_items) * self.shipping_cost)


if __name__ == '__main__':
    sh = Order(20, 1, Ground(['a', 'b', 'c'], 3))
    print(sh.shipping.get_cost(), sh.shipping.get_date())

    sh_air = Order(20, 1, Air(['a', 'b', 'c'], 3))
    print(sh_air.shipping.get_cost(), sh_air.shipping.get_date())
