from editor import *


if __name__ == '__main__':
    app = Application()
    app.editors['text_edit'] = Editor()
    app.active_editor = app.editors['text_edit']
    app.create_ui()

    app.cut_button.click()
    app.copy_button.click()
    app.cut_button.click()
    app.paste_button.click()
    # app.undo_button.click()
    print(app.history._history)
    for h in app.history._history:
        print(h.__dict__)
