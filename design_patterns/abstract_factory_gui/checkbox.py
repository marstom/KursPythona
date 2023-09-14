import abc


class Checkbox(abc.ABC):
    @abc.abstractmethod
    def render(self):
        ...

    @abc.abstractmethod
    def on_click(self, action):
        ...


class WinCheckbox(Checkbox):
    def render(self):
        print("Rendered Windows checkbox")

    def on_click(self, action):
        print("Clicked widnows checkbox")


class HTMLCheckbox(Checkbox):
    def render(self):
        print("Rendered HTML checkbox")

    def on_click(self, action):
        print("Clicked HTML checkbox")

class IOSCheckbox(Checkbox):
    def render(self):
        print("Rendered IOS checkbox")

    def on_click(self, action):
        print("Clicked IOS checkbox")
