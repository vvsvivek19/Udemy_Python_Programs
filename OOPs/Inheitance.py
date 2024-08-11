class Rectangle:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b
        Rectangle.count += 1

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length * self.breadth)


class Cuboid(Rectangle):
    def __init__(self,l,b,h):
        self.height = h
        super().__init__(l,b) #Constructor Overloading

    def volume(self):
        return self.length * self.breadth * self.height
