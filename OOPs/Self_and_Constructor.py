class Cuboid:
    def __init__(self, l, b, h):
        print(id(self))
        self.length = l
        self.breadth = b
        self.height = h

    def lidarea(self):
        print(id(self))
        return self.length * self.breadth

    def totalarea(self):
        return 2 * (self.breadth * self.length + self.length * self.height + self.breadth * self.height)

    def volume(self):
        return self.length * self.breadth * self.height


c1 = Cuboid(10, 5, 3)
print(id(c1))
c1.lidarea()
print('')
c2 = Cuboid(20, 10, 5)
print(id(c2))
c2.lidarea()
