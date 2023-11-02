class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def display_dimensions(self):
        print("width = " + str(self.width) + "| height = " + str(self.height))

    def perimeter(self):
        print(self.height * 2 + self.width * 2)


class Square(Rectangle):
    def __init__(self, side_length):
        Rectangle.__init__(self, side_length, side_length)


square1 = Square(4)
square1.display_dimensions()
square1.perimeter()
