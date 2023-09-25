from typing import Protocol
from random import randint


class Character:
    def __init__(self, strategy: "Strategy"):
        self.strategy = strategy

    def attack_opponent(self):
        self.strategy.attack()

class Strategy(Protocol):
    def attack(self):
        ...


class Bow(Strategy):
    def attack(self):
        print(f"Range damage {randint(2, 50)}")


class Sword(Strategy):
    def attack(self):
        print(f"Sword damage {randint(20, 50)}")


class Magic(Strategy):
    def attack(self):
        print(f"Magic damage {randint(15, 30)}")


if __name__ == '__main__':
    ch = Character(Sword())
    ch.attack_opponent()
    ch.strategy = Bow()
    ch.attack_opponent()
    ch.strategy = Magic()
    ch.attack_opponent()
