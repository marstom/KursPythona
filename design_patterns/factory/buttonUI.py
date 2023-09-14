import abc
from button import Button, WinButton, HTMLButton, IOSButton


class Dialog(abc.ABC):
    def render(self):
        button: Button = self.create_button()
        button.on_click("close")
        button.render()

    @abc.abstractmethod
    def create_button(self):
        ...


class WindowsDialog(Dialog):

    def create_button(self) -> Button:
        return WinButton()



class HTMLDialog(Dialog):

    def create_button(self) -> Button:
        return HTMLButton()

class IOSDialog(Dialog):

    def create_button(self) -> Button:
        return IOSButton()
