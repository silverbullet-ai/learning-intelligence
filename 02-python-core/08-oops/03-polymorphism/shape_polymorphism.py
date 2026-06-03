class Shape:

    def area(self):

        return 0


class Circle(Shape):

    def __init__(self, radius):

        self.radius = radius

    def area(self):

        return 3.14 * self.radius * self.radius


class Rectangle(Shape):

    def __init__(self, width, height):

        self.width = width
        self.height = height

    def area(self):

        return self.width * self.height


def print_area(shape):

    print(shape.area())


circle = Circle(3)
rectangle = Rectangle(4, 5)

print_area(circle)
print_area(rectangle)