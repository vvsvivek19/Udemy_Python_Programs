from math import *

class Shape:
    def __init__(self,name):
        self.name = name
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,l,b):
        self.length = l
        self.breadth = b
    def area(self):
        return 0.5 * self.length * self.breadth

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return pi * (self.radius ** 2)

r = Rectangle(10,5)
print(r.area())

c = Circle(10)
print(round(c.area(),2))

