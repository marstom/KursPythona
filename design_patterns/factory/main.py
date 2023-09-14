from buttonUI import HTMLDialog, WindowsDialog, IOSDialog, Dialog


def read_conf_file():
    return {
        # "OS": "Windows",
        # "OS": "WEB",
        "OS": "IOS",
    }


class App:
    def __init__(self):
        self.dialog: Dialog

    def init(self):
        conf = read_conf_file()

        if conf.get("OS") == "Windows":
            self.dialog = WindowsDialog()
        elif conf.get("OS") == "WEB":
            self.dialog = HTMLDialog()
        elif conf.get("OS") == "IOS":
            self.dialog = IOSDialog()
        else:
            raise Exception("Invalid os")


if __name__ == '__main__':
    app = App()
    app.init()
    app.dialog.render()
