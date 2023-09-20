import abc
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from editor import Application, Editor

class Command(abc.ABC):
    def __init__(self, app: "Application", editor: "Editor"):
        self._app = app
        self._editor = editor
        self._backup = dict()

    def save_backup(self):
        self._backup = self._editor.text

    def undo(self):
        self._editor.text = self._backup

    @abc.abstractmethod
    def execute(self):
        ...


class CommandHistory:
    def __init__(self):
        self._history: list[Command] = []

    def push(self, c: Command):
        self._history.append(c)

    def pop(self) -> Command:
        return self._history.pop()


class CopyCommand(Command):
    def execute(self):
        print("copy")
        self._app = self._editor.get_selection()
        return False


class CutCommand(Command):
    def execute(self):
        print("cut")
        self._app.clipboard = self._editor.get_selection()
        self._editor.delete_selection()
        return True


class PasteCommand(Command):
    def execute(self):
        print("paste")
        self.save_backup()
        self._editor.replace_selection(self._app.clipboard)
        return True


class UndoCommand(Command):
    def execute(self):
        print("undo")
        self._app.undo()
        return False
