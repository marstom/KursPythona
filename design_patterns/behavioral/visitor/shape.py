from typing import Protocol, Callable


class Shape(Protocol):
    def move(self, x, y):
        ...

    def draw(self):
        ...

    def accept(self, v: "Visitor"):
        ...


class Dot(Shape):
    def __init__(self, screen: "Surface", draw_fn: Callable, color: tuple):
        self._screen = screen
        self._draw_fn = draw_fn
        self._color = color

        self._x = 0
        self._y = 0

    def move(self, x, y):
        self._x += x
        self._y += y

    def draw(self):
        for i in range(self._x, 15 + self._x):
            for j in range(self._y, 15 + self._y):
                self._draw_fn(self._screen, i, j, self._color)

    def accept(self, v: "Visitor"):
        return v.visit_dot(self)


class Rectangle(Shape):
    def __init__(self, screen: "Surface", draw_fn: Callable, rect: "Rect", color: tuple):
        self._screen = screen
        self._draw_fn = draw_fn
        self._color = color

        self._rect = rect

    def move(self, x, y):
        self._rect.left += x
        self._rect.top += y

    def draw(self):
        self._draw_fn(surface=self._screen, color=self._color, rect=self._rect, border_radius=2)

    def accept(self, v: "Visitor"):
        return v.visit_rectangle(self)


class Circle(Shape):
    def __init__(self, screen: "Surface", draw_fn: Callable, color: tuple, radius: int):
        self._screen = screen
        self._draw_fn = draw_fn
        self._color = color

        self._center_x = 0
        self._center_y = 0
        self._radius = radius

    def move(self, x, y):
        self._center_x += x
        self._center_y += y

    def draw(self):
        self._draw_fn(self._screen, self._color, (self._center_x, self._center_y), self._radius)

    def accept(self, v: "Visitor"):
        return v.visit_circle(self)


class Visitor(Protocol):
    def visit_dot(self, d: "Dot"):
        ...

    def visit_rectangle(self, r: "Rectangle"):
        ...

    def visit_circle(self, r: "Circle"):
        ...


class JSONVisitor(Visitor):
    def visit_dot(self, d: "Dot"):
        return {
            "x": d._x,
            "y": d._y,
        }

    def visit_rectangle(self, r: "Rectangle"):
        return {
            "w": r._rect.width,
            "h": r._rect.height,
            "top": r._rect.top,
            "left": r._rect.left,
        }

    def visit_circle(self, c: "Circle"):
        return {
            "x": c._center_x,
            "y": c._center_y,
            "radius": c._radius,
        }
