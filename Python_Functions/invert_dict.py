def invert(d):
    newd = {}
    for x,y in d.items():
        newd[y] = x
    return newd


D = {'a':10,'b':20,'c':30,'d':40,'e':50}
print("Reverse of dictionary is:",invert(D))