import abc

from button import Button, WinButton, HTMLButton, IOSButton
from checkbox import Checkbox, WinCheckbox, HTMLCheckbox, IOSCheckbox


class GUIFactory(abc.ABC):
    @abc.abstractmethod
    def create_button(self) -> Button:
        ...

    @abc.abstractmethod
    def create_checkbox(self) -> Checkbox:
        ...


class WinFactory(GUIFactory):
    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()


class HTMLFactory(GUIFactory):
    def create_button(self) -> Button:
        return HTMLButton()

    def create_checkbox(self) -> Checkbox:
        return HTMLCheckbox()

class IOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return IOSButton()

    def create_checkbox(self) -> Checkbox:
        return IOSCheckbox()