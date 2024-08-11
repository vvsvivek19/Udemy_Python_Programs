n = int(input("How many numbers you want to enter?: "))
psum = 0
nsum = 0
while n != 0:
    num = int(input("Enter a number: "))
    if num > 0:
        psum = psum + num
    else:
        nsum = nsum + (num)
    n -= 1
print("Sum of the positive numbers is:", psum)
print("Sum of the negative numbers is:", nsum)