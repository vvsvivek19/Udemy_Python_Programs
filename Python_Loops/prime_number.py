num = int(input("Please enter a number = "))
flag = 0
for n in range(2, num):
    if num % n == 0:
        flag = 1
        break

if flag == 0:
    print("Number is prime!")
else:
    print("Not a prime!")