def fun2(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for x in kwargs:
        print(x,':',kwargs[x])

fun2(name='Ajay', Rollo='10',Address='Delhi')