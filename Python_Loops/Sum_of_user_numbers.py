n = int(input("How many numbers you want to enter?: "))
sum = 0
while n != 0:
    num = int(input("Enter a number: "))
    sum = sum + num
    n -= 1
print("Sum of the given numbers is:", sum)