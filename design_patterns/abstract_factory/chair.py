import abc


class Chair(abc.ABC):
    @abc.abstractmethod
    def has_legs(self) -> bool:
        ...

    @abc.abstractmethod
    def sit_on(self) -> None:
        ...


class VictorianChair(Chair):
    def has_legs(self) -> bool:
        return True

    def sit_on(self) -> None:
        print("Sit on victorian chair")


class ModernChair(Chair):
    def has_legs(self) -> bool:
        return True

    def sit_on(self) -> None:
        print("Sit on modern chair")
