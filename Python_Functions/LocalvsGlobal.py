
def fun1(a, b):
    c = a + b
    print('Local:', c)
    print('Global:', g)

g = 10

fun1(4,8)

