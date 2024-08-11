from math import *


class Polygon:
    def __init__(self, no_of_sides, *sides):
        self.no_of_sides = no_of_sides
        self.sides = sides[:no_of_sides]  #slicing


class Triangle(Polygon):
    def __init__(self, no_of_sides, *sides):
        super().__init__(no_of_sides, *sides)

    def area(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = sqrt(s * (s - a) * (s - b) * (s - c))
        print('Area of Given Triangle: ', round(area, 2))


t1 = Triangle(3, 10, 15, 9, 2)
t1.area()
