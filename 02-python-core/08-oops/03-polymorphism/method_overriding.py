class Shape:

    def area(self):

        return "Area not defined"


class Rectangle(Shape):

    def __init__(self, width, height):

        self.width = width
        self.height = height

    def area(self):

        return self.width * self.height


rectangle = Rectangle(4, 5)

print(rectangle.area())