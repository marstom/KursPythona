from gui_with_help import *


# import heartrate
# heartrate.trace(browser=True)

if __name__ == '__main__':
    dialog = Dialog("My windom")
    dialog.tooltip_text = "Here is dialog tooltip text."
    # more important is wiki in chaint
    dialog.wiki_page_url = 'www.wiki../..././'

    panel = Panel(22, 33, 800, 600)
    # panel.modal_help_text = "Panel modal"

    ok = Button(23, 23, "Ok")
    ok.tooltip_text = "Tooltip button ok"

    cancel = Button(23, 23, "Cancel")
    cancel.tooltip_text = "Tooltip button cancel"

    panel.add(ok)
    panel.add(cancel)
    dialog.add(panel)

    # move mouse to GUI element:
    panel.show_help()
    dialog.show_help()
    cancel.show_help()
    ok.show_help()


