class Shape(object):
    """Makes shapes!"""

    def __init__(self, number_of_sides: int):
        self.number_of_sides = number_of_sides

# Add your Triangle class below!


class Triangle(Shape):
    def __init__(self, side1: int, side2: int, side3: int):
        super().__init__(3)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
