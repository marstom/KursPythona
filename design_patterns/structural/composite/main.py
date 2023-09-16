from graphic import Graphic, Dot, Circle, CompoundGraphic


class ImageEditor:
    all: CompoundGraphic

    def load(self):
        self.all = CompoundGraphic()
        self.all.add(Dot(1, 2))
        self.all.add(Dot(2, 4))
        self.all.add(Circle(5, 3, 10))

    def groupSelected(self, components: list[Graphic]):
        group = CompoundGraphic()
        for component in components:
            group.add(component)
            self.all.remove(component)
        self.all.add(group)
        self.all.draw()

if __name__ == '__main__':
    imged = ImageEditor()
    imged.load()

    imged.groupSelected([Dot(1,2), Dot(2,2)])
