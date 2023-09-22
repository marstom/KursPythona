import abc

from pydantic import BaseModel


class Options(BaseModel):
    voltage: int
    password: str


class EngineContext:

    def __init__(self, state: "State"):
        """Engine in the initial state"""
        self._speed = 0
        self._running = False
        self._options = Options(voltage=0, password="")
        self.transition_to(state)

    def transition_to(self, state: "State"):
        print(f"EngineContext: Transition to :: {type(state).__name__}")
        self._state = state
        self._state.context = self

    def push_on_off(self):
        self._state.push_on_off()

    def set_options(self, opts: Options):
        self._state.set_options(opts)

    def set_speed(self, s: int):
        self._state.set_speed(s)


class State(abc.ABC):
    # def __init__(self):
    #     self._engine: "EngineContext" = None

    @property
    def context(self) -> "EngineContext":
        return self._engine

    @context.setter
    def context(self, engine: EngineContext):
        self._engine = engine

    @abc.abstractmethod
    def push_on_off(self):
        ...

    @abc.abstractmethod
    def set_speed(self, speed: int):
        ...

    @abc.abstractmethod
    def set_options(self, options: Options):
        ...


class OffState(State):
    def push_on_off(self):
        print("Engine start procedure...")
        self.context.transition_to(SelfTestState())

    def set_speed(self, speed: int):
        print("Can't set speed on off state")

    def set_options(self, options: Options):
        print("Can't set options on off state")


class SelfTestState(State):
    def push_on_off(self):
        print("Can't on/off in set options state")

    def set_speed(self, speed: int):
        print("Can't set speed in set options state")

    def set_options(self, options: Options):
        if options.voltage > 10 and options.voltage < 120:
            self._engine._options = options
            print(f"options has been set {options}")
            self.context.transition_to(ChangeSpeedState())
        else:
            print(f"Wrong parameters, voltage out of range {options.voltage}!!!")
            self.context.transition_to(SelfTestState())


class ChangeSpeedState(State):
    def push_on_off(self):
        print("Can't on/off in change speed state")

    def set_speed(self, speed: int):
        self._engine._speed = speed
        print(f"speed set {speed}")
        self.context.transition_to(RunState())

    def set_options(self, options: Options):
        print("Can't set_options in change speed state")


class RunState(State):
    def push_on_off(self):
        print(f"Off....")
        self.context.transition_to(OffState())

    def set_speed(self, speed: int):
        print(f"Transition to set speed...")
        self._engine._speed = speed
        print(f"speed set {speed}")
        self.context.transition_to(RunState())

    def set_options(self, options: Options):
        print("Can't set_options in run state")
