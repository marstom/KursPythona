from memento import State, Editor, Command


def test_editor():
    editor = Editor()
    editor.state = State(x=22, y=33, text="Tom")
    assert editor.state.dict() == {'x': 22, 'y': 33, 'text': 'Tom'}


def test_editor_snapshot_restore():
    editor = Editor()
    editor.state = State(x=22, y=33, text="Tom")
    assert editor.state.dict() == {'x': 22, 'y': 33, 'text': 'Tom'}

    snapshot = editor.create_snapshot()
    editor.state = State(x=1, y=2, text="Mark")
    assert editor.state.dict() == {'x': 1, 'y': 2, 'text': 'Mark'}
    snapshot.restore()
    assert editor.state.dict() == {'x': 22, 'y': 33, 'text': 'Tom'}


def test_editor_snapshot_restore_multiple():
    editor = Editor()
    editor.state = State(x=22, y=33, text="Tom")
    snapshot = editor.create_snapshot()
    assert editor.state.dict() == {'x': 22, 'y': 33, 'text': 'Tom'}

    editor.state = State(x=1, y=33, text="Tom")
    snapshot2 = editor.create_snapshot()
    assert editor.state.dict() == {'x': 1, 'y': 33, 'text': 'Tom'}

    editor.state = State(x=2, y=33, text="Tom")
    snapshot3 = editor.create_snapshot()
    assert editor.state.dict() == {'x': 2, 'y': 33, 'text': 'Tom'}

    snapshot3.restore()
    assert editor.state.dict() == {'x': 2, 'y': 33, 'text': 'Tom'}

    snapshot2.restore()
    assert editor.state.dict() == {'x': 1, 'y': 33, 'text': 'Tom'}

    snapshot.restore()
    assert editor.state.dict() == {'x': 22, 'y': 33, 'text': 'Tom'}


def test_command():
    editor = Editor()
    editor.state = State(x=0, y=0, text="Tox")

    command = Command(editor)
    command.make_backup()

    editor.state = State(x=1, y=0, text="Tom")
    command.make_backup()
    assert editor.state.dict() == {'x': 1, 'y': 0, 'text': 'Tom'}

    editor.state = State(x=2, y=0, text="Tom")
    command.make_backup()
    assert editor.state.dict() == {'x': 2, 'y': 0, 'text': 'Tom'}

    editor.state = State(x=3, y=0, text="Tom")
    command.make_backup()
    assert editor.state.dict() == {'x': 3, 'y': 0, 'text': 'Tom'}


    command.undo()
    assert editor.state.dict() == {'x': 3, 'y': 0, 'text': 'Tom'}
    command.undo()
    assert editor.state.dict() == {'x': 2, 'y': 0, 'text': 'Tom'}
    command.undo()
    assert editor.state.dict() == {'x': 1, 'y': 0, 'text': 'Tom'}
    command.undo()
    assert editor.state.dict() == {'x': 0, 'y': 0, 'text': 'Tox'}
    command.undo() # no more backups
    assert editor.state.dict() == {'x': 0, 'y': 0, 'text': 'Tox'}
