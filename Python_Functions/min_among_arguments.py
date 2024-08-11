def minimum(*args, low_limit=None):
    if low_limit == None:
        x = min(args)
        return x
    else:
        L = []
        for i in args:
            if i >= low_limit:
                L.append(i)
        x = min(L)
        return x


print(minimum(1,5,2,-5,10))
print(minimum(1,5,2,-5,10, low_limit=0))
