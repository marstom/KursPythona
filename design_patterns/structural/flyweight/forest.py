import pygame

# this is flyweight
# memory heavy class that we reuse
# this should be immutable.
class TreeType:
    def __init__(self, name, color, texture):
        self._texture = texture
        self._color = color
        self._name = name

    def draw(self, canvas, x, y):
        print(f"HEAVY: draw on canvas: {canvas} tree: {self._name}, pos: {x} {y}")


class TreeFactory:
    # it can also by a dict!
    tree_types: list[TreeType] = []

    @classmethod
    def get_tree_type(cls, name, color, texture):
        filtered = list(filter(lambda tree: tree._name == name
                            and tree._color == color
                            and tree._texture == texture,
                               cls.tree_types))
        if len(filtered) == 0:
            print(f"creatate new flyweight!!! | {name} {color} {texture}")
            new_type = TreeType(name, color, texture)
            cls.tree_types.append(new_type)
            return new_type
        elif len(filtered) != 1:
            raise Exception("More than 1 the same trees in trees base.")
        return filtered[0]


class Tree:
    def __init__(self, x, y, tree_type):
        self.x: int = x
        self.y: int = y
        self.type: TreeType = tree_type

    def draw(self, canvas):
        print(f"light: draw on canvas: {canvas} a tree type: {self.type._name} {self.type._color} {self.type._texture}, pos: {self.x} {self.y}")


class Forest:
    def __init__(self):
        self.trees: list[Tree] = []

    def plant_tree(self, x, y, name, color, texture) -> Tree:
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self, canvas):
        for tree in self.trees:
            tree.draw(canvas)
