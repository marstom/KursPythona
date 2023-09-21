from pydantic import BaseModel


class State(BaseModel):
    x: int
    y: int
    text: str


class Snapshot:
    def __init__(self, editor: "Editor", state: State):
        self.__editor = editor
        self.__state: State = state

    def restore(self):
        self.__editor.state = self.__state

class Editor:
    def __init__(self):
        self.__state: State = State(x=0, y=0,text= "")

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state: State):
        self.__state = state


    def create_snapshot(self):
        return Snapshot(self, self.__state)


class Command:
    def __init__(self, editor: Editor):
        self.__editor = editor
        self.__backups: list[Snapshot] = []

    def make_backup(self):
        self.__backups.append(self.__editor.create_snapshot())

    def undo(self):
        if self.__backups:
            backup = self.__backups.pop()
            backup.restore()
            return True
        else:
            print("No more backups...")
            return False
