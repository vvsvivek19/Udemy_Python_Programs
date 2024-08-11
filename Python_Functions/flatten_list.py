def flatten(l):
    for e in l:
        if hasattr(e, '__iter__'):
            yield from flatten(e)
        else:
            yield e
L = [1,2,[3,4,[5,6],7],8]
f = flatten(L)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))