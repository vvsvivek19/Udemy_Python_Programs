n = int(input("Enter a number: "))
temp = n
bin = ""
while temp != 0:
    r = temp % 2
    bin = str(r) + bin
    temp = temp // 2
#Below method can give a correct binary number for odd numbers. We will always lose
#all the zeros when we create a binary number for even numbers.
# while rev_bin != 0:
#     r = rev_bin % 10
#     bin = bin * 10 + r
#     rev_bin = rev_bin // 10
print("Binary of", n, "is", bin)