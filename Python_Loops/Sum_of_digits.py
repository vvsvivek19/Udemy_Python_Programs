n = int(input("Enter a number: "))
sum = 0
while n > 0:
    r = n % 10
    sum = sum + r
    n = n // 10
print("Sum of digits of the given number is:", sum)