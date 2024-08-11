class Angle:
    def __init__(self, deg=0):
        self.degree = deg

    def __add__(self, Ang):
        Sum = Angle()
        Sum.degree = self.degree + Ang.degree
        return Sum

    def __str__(self):
        return str(self.degree)
a1 = Angle(60)
a2 = Angle(70)
s = a1 + a2
print(s)