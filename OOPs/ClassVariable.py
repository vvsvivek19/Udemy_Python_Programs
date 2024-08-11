class Rectangle:
    count = 0

    def __init__(self,l,b):
        self.length = l
        self.breadth = b
        Rectangle.count += 1

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length * self.breadth)

    @classmethod
    def CountRect(cls):
        print(cls.count)

r1 = Rectangle(10,15)
r2 = Rectangle(40,25)
r3 = Rectangle(10,15)

Rectangle.CountRect()

