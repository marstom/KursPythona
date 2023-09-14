import abc
from button import Button, WinButton, HTMLButton, IOSButton

from gui_factory import GUIFactory

"""
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
"""

class Application:
    factory: GUIFactory
    button: Button

    def __init__(self, factory: GUIFactory):
        self.factory = factory

    def create_ui(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()

    def paint(self):
        self.button.render()
        self.checkbox.render()
