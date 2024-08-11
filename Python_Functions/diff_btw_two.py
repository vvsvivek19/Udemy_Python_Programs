def diff(num1, num2):
    sub = abs(num1 - num2)
    if sub <= 5:
        print('Difference is', sub)
    else:
        print("Cannot print difference, it is greater than 5")


dig1 = int(input("Please Enter first Number: "))
dig2 = int(input("Please Enter second number: "))
diff(dig1,dig2)
