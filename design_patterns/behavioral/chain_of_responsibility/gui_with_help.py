from typing_extensions import Protocol

# import heartrate
# heartrate.trace()

class ComponentWithContextualHelp(Protocol):
    def show_help(self):
        ...


class Component(ComponentWithContextualHelp):
    def __init__(self):
        self._container: Container = None
        self.tooltip_text: str = ""

    def show_help(self):
        print(f"Showing component general tooltip: {self.tooltip_text}")


class Container(Component):
    def __init__(self):
        super().__init__()
        self._children: list[Component] = []

    def add(self, child: Component):
        print(f"Added: {child} to {self}")
        self._children.append(child)
        child._container = self


class Button(Component):
    def __init__(self, x, y, text):
        super().__init__()
        self.y = y
        self.x = x
        self.text = text


class Panel(Container):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.height = height
        self.width = width
        self.y = y
        self.x = x
        self.modal_help_text: str = ""

    def show_help(self):
        if self.modal_help_text:
            print(f"Show modal help text for panel: {self.modal_help_text}")
        else:
            super().show_help()


class Dialog(Container):
    def __init__(self, title):
        super().__init__()
        self.title = title
        self.wiki_page_url: str = ""

    def show_help(self):
        if self.wiki_page_url:
            print("Open wiki page for dialog")
        else:
            super().show_help()
