print('Before Try')
try:
    a = int(input("Enter Numerator: "))
    b = int(input("Enter Denominator: "))
    c = a // b
    print('Try Block executed successfully')
except (ZeroDivisionError, ValueError) as err:
    print(err)
else:
    print("Division is", c)
finally:
    print("Finally Block")

print('outside try-except block')