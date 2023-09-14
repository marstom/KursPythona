from enum import Enum


class ShType(Enum):
    GROUND = "GROUND"
    AIR = "AIR"


class Order:
    def __init__(self, line_items: list, shipping_cost: int, shipping: ShType):
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

    def get_shipping_date(self):
        return "12-12-2022"


if __name__ == '__main__':
    ord = Order(['a', 'b', 'c'], 2, ShType.AIR)
    print("Shiping : ", ord.get_shipping_cost(), "$", " date: ", ord.get_shipping_date())

    ord_g = Order(['a', 'b', 'c'], 2, ShType.GROUND)
    print("Shiping : ", ord_g.get_shipping_cost(), "$", " date: ", ord_g.get_shipping_date())
