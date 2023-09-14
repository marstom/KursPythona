import abc


class Button(abc.ABC):
    @abc.abstractmethod
    def render(self):
        ...

    @abc.abstractmethod
    def on_click(self, action):
        ...


class WinButton(Button):
    def render(self):
        print("Rendered Windows button")

    def on_click(self, action):
        print("Clicked widnows button")


class HTMLButton(Button):
    def render(self):
        print("Rendered HTML button")

    def on_click(self, action):
        print("Clicked HTML button")

class IOSButton(Button):
    def render(self):
        print("Rendered IOS button")

    def on_click(self, action):
        print("Clicked IOS button")
