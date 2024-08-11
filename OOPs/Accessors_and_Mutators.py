class Rectangle:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b
    def getLength(self):
        return self.length
    def setLength(self,l):
        self.length = l
    def getBreadth(self):
        return self.breadth
    def setBreadth(self,b):
        self.breadth = b
    def area(self):
        return  self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)

r1 = Rectangle(10,5)
print(r1.getLength())
r1.setLength(15)
print(r1.area())
