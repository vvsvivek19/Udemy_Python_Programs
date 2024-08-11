class Rational:
    def __init__(self,num=1,deno=1):
        self.p = num
        self.q = deno
    def __add__(self, other):
        sum = Rational()
        sum.p = self.p*other.q + other.p*self.q
        sum.q = self.q * other.q
        return sum
    def __sub__(self, other):
        sub = Rational()
        sub.p = self.p * other.q - other.p * self.q
        sub.q = self.q * other.q
        return sub
    def __str__(self):
        return str(self.p) + '/' + str(self.q)
A = Rational(2,3)
B = Rational(1,2)
C = A + B
D = A - B
print(C)
print(D)
