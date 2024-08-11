from math import *

class Circle:
    def __init__(self,r):
        self.radius = r
    def area(self):
        return pi * (self.radius**2)
    def perimeter(self):
        return 2 * pi * self.radius

c1 = Circle(9)
print('Area:',round(c1.area(),2))
print('Perimeter: ',round(c1.perimeter(),2))