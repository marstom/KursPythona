import abc


class Engine(abc.ABC):
    hp = None

    @abc.abstractmethod
    def start(self):
        ...

    @abc.abstractmethod
    def stop(self):
        ...


class SportEngine(Engine):
    hp = 250

    def start(self):
        print(f"Started! : {self.hp}HP Sport")

    def stop(self):
        print("Stop! : 0HP Sport")


class StandardEngine(Engine):
    hp = 80

    def start(self):
        print(f"Started! : {self.hp}HP Standard")

    def stop(self):
        print("Stop! : 0HP Standard")
