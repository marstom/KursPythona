from shape import Shape, Circle, Rectangle


def business_logic(shapes: list[Shape]):
    shc: list[Shape] = []

    # allow us copy this without knowledge about the object
    for sh in shapes:
        shc.append(sh.clone())
    print("Here are copies")
    for s in shc:
        print(s.__dict__)


if __name__ == '__main__':
    shapes: list[Shape] = []

    circle = Circle()
    circle.x = 2
    circle.y = 3
    circle.radius = 10
    shapes.append(circle)

    another_circle = circle.clone()
    another_circle.x = 222
    another_circle.radius = 222
    shapes.append(another_circle)

    rectangle = Rectangle()
    rectangle.x = 6
    rectangle.y = 7
    rectangle.width = 10
    rectangle.height = 20
    shapes.append(rectangle)

    business_logic(shapes)
