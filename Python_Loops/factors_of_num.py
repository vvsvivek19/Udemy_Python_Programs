num = int(input("Please enter a number = "))
print("Factors of given number are = ")
for n in range(1,num+1):
    if num % n == 0:
        print(n)