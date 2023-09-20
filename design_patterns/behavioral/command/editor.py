from typing import Callable

from command import *


class Editor:
    def __init__(self):
        self.text = ""

    def get_selection(self):
        return "this is selectd text"

    def delete_selection(self):
        print("Deleted selected text...")

    def replace_selection(self, text):
        print(f"Replaced selected text to: {text}")


# UI elements
class Button:
    def __init__(self):
        self._command: Callable

    def set_command(self, command: Command):
        self._command = command

    def click(self):
        self._command()


##
class Application:
    def __init__(self):
        self.editors: list[Editor] = dict()
        self.active_editor: Editor = None
        self.clipboard = ""
        self.history = CommandHistory()

    def create_ui(self):
        print("You can see beautiful ui:")
        print("You have copy, cut, delete, undo buttons...")

        self.copy_button = Button()
        def copy():
            self.exectue_command(CopyCommand(self, self.active_editor))
        self.copy_button.set_command(copy)

        self.cut_button = Button()
        def cut():
            self.exectue_command(CutCommand(self, self.active_editor))
        self.cut_button.set_command(cut)

        self.paste_button = Button()
        def paste():
            self.exectue_command(PasteCommand(self, self.active_editor))
        self.paste_button.set_command(paste)

        self.undo_button = Button()
        def undo():
            self.exectue_command(UndoCommand(self, self.active_editor))
        self.undo_button.set_command(undo)

    def exectue_command(self, c: Command):
        if c.execute():
            self.history.push(c)

    def undo(self):
        comm = self.history.pop()
        if comm:
            comm.undo()
