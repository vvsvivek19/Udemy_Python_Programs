def div(a,b):
    if b != 0:
        c = a // b
        return c
    else:
        raise ZeroDivisionError


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

try:
    res = div(a,b)
    print(res)
except:
    print("ZeroDivisionError")