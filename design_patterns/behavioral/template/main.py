import abc


class Template(abc.ABC):

    def open_file(self):
        print("Open file")

    @abc.abstractmethod
    def parse(self):
        ...

    def save_file(self):
        print("Save file")


class CSV(Template):
    def parse(self):
        print("Parse CSV")


class YML(Template):
    def parse(self):
        print("Parse YAML")


if __name__ == '__main__':
    csv = CSV()
    csv.open_file()
    csv.parse()
    csv.save_file()

    yml = YML()
    yml.open_file()
    yml.parse()
    yml.save_file()
