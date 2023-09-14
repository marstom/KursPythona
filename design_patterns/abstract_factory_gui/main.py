from gui_factory import WinFactory, HTMLFactory, GUIFactory, IOSFactory
from application import Application


def read_conf_file():
    return {
        # "OS": "Windows",
        # "OS": "WEB",
        "OS": "IOS",
    }


if __name__ == '__main__':
    factory: GUIFactory
    conf = read_conf_file()

    if conf.get("OS") == "Windows":
        factory = WinFactory()
    elif conf.get("OS") == "WEB":
        factory = HTMLFactory()
    elif conf.get("OS") == "IOS":
        factory = IOSFactory()
    else:
        raise Exception("Invalid os")
    app = Application(factory)
    app.create_ui()
    app.paint()
