def greater_three(a,b,c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


num1 = int(input("Enter a Number: "))
num2 = int(input("Enter a Number: "))
num3 = int(input("Enter a Number: "))

print("Greatest among the entered three numbers is",greater_three(num1,num2,num3))