class Triangle(object):
    number_of_sides = 3

    def __init__(self, angle1: int, angle2: int, angle3: int):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        return self.angle1 + self.angle2 + self.angle3 == 180

my_triangle = Triangle(90,30,60)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())