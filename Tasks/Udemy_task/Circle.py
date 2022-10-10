from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * pi * self.radius


circle = Circle(10)
area = circle.get_area()
print(area)
perimeter = circle.get_perimeter()
print(perimeter)
