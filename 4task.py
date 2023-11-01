class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        print(str(self.color) + " figure")


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def display_dimensions(self):
        print("width = " + str(self.width) + "| height = " + str(self.height))

    def display_color(self):
        print(str(self.color) + " rectangle")
        self.display_dimensions()

rec1 = Rectangle("red", 12, 4)
rec1.display_color()

