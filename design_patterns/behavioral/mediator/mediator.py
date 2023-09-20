import abc

from typing_extensions import Protocol


class Component(abc.ABC):
    def __init__(self, mediator: "Mediator" = None):
        self._mediator = mediator

    @abc.abstractmethod
    def launch(self):
        ...

    @abc.abstractmethod
    def land(self):
        ...


class Mediator(Protocol):
    def notify(self, sender: Component, event: str):
        ...


class Tower(Mediator):
    def __init__(self, helicopter, plane_red, plane_green, plane_blue):
        self.name = "Main Tower"
        self.moves = list()

        self._helicopter = helicopter
        self._helicopter._mediator = self
        self._plane_blue = plane_blue
        self._plane_blue._mediator = self
        self._plane_green = plane_green
        self._plane_green._mediator = self
        self._plane_red = plane_red
        self._plane_red._mediator = self

    def notify(self, sender: Component, event: str):
        print(f"EVENT: {sender} {event}")
        if sender is self._helicopter and event == "launch":
            self._plane_red.wait()
            self._plane_green.launch()

        if sender is self._plane_red and event == "wait":
            self._helicopter.clear_way()

        if event == "land":
            self._helicopter.clear_way()
            self._plane_blue.clear_way()
            self._plane_red.clear_way()
            self._plane_green.clear_way()


class Helicopter(Component):
    def launch(self):
        print("Helicopter lanunch")
        self._mediator.notify(self, "launch")

    def land(self):
        print("Helicopter land")
        self._mediator.notify(self, "land")

    def clear_way(self):
        print("It's clear way to take off...")


class PlaneRed(Component):
    def launch(self):
        print("RedPlane lanunch")
        self._mediator.notify(self, "launch")

    def land(self):
        print("RedPlane land")
        self._mediator.notify(self, "land")

    def wait(self):
        print("RedPlan: I need wait ...")
        self._mediator.notify(self, "wait")

    def clear_way(self):
        print("It's clear way to take off...")


class PlaneGreen(Component):
    def launch(self):
        print("GreenPlane lanunch")
        self._mediator.notify(self, "launch")

    def land(self):
        print("GreenPlane land")
        self._mediator.notify(self, "land")

    def clear_way(self):
        print("It's clear way to take off...")


class PlaneBlue(Component):

    def launch(self):
        print("BluePlane lanunch")
        self._mediator.notify(self, "launch")

    def land(self):
        print("BluePlane land")
        self._mediator.notify(self, "land")

    def clear_way(self):
        print("It's clear way to take off...")
