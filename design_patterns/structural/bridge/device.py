import abc


class Device(abc.ABC):
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        ...

    @abc.abstractmethod
    def enable(self):
        ...

    @abc.abstractmethod
    def disable(self):
        ...

    @abc.abstractmethod
    def get_volume(self) -> int:
        ...

    @abc.abstractmethod
    def set_volume(self, percent: int):
        ...

    @abc.abstractmethod
    def get_channel(self) -> int:
        ...

    @abc.abstractmethod
    def set_channel(self, ch: int):
        ...


class Radio(Device):
    def __init__(self):
        self.__enabled = False
        self.__volume = 0
        self.__ch = 0

    def is_enabled(self) -> bool:
        return self.__enabled

    def enable(self):
        self.__enabled = True

    def disable(self):
        self.__enabled = False

    def get_volume(self) -> int:
        return self.__volume

    def set_volume(self, percent: int):
        if 0 <= percent <= 100:
            self.__volume = percent

    def get_channel(self) -> int:
        return self.__ch

    def set_channel(self, ch: int):
        self.__ch = ch


class TV(Device):
    def __init__(self):
        self.__enabled = False
        self.__volume = 0
        self.__ch = 0

    def is_enabled(self) -> bool:
        return self.__enabled

    def enable(self):
        self.__enabled = True

    def disable(self):
        self.__enabled = False

    def get_volume(self) -> int:
        return self.__volume

    def set_volume(self, percent: int):
        if 0 <= percent <= 10:
            self.__volume = percent

    def get_channel(self) -> int:
        return self.__ch

    def set_channel(self, ch: int):
        self.__ch = ch
