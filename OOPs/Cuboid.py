class Cuboid:
    def __init__(self, l, b, h):
        self.length = l
        self.breadth = b
        self.height = h

    def lidarea(self):
        return self.length * self.breadth

    def totalarea(self):
        return 2 * (self.breadth * self.length + self.length * self.height + self.breadth * self.height)

    def volume(self):
        return self.length * self.breadth * self.height


c1 = Cuboid(10, 5, 3)
print(c1.volume())
c1.height = 30
print(c1.volume())
c2 = Cuboid(20, 10, 5)
print(c2.volume())
