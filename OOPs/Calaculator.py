class Calculator:
    @staticmethod
    def add(a,b):
        return  a+b
    @staticmethod
    def sub(a,b):
        return a-b
    @staticmethod
    def mul(a,b):
        return a*b
    @staticmethod
    def div(a,b):
        return a/b

c1 = Calculator()
print(c1.add(5,6))
print(c1.sub(7,8))
print(c1.mul(78,8))
print(round(c1.div(98,9),2))