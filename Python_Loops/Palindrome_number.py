n = int(input("Enter a number: "))
temp = n
reverse = 0
while temp > 0:
    r = temp % 10
    reverse = (reverse * 10) + r
    temp = temp // 10
if n == reverse:
    print("Given number is palindrome")
else:
    print("Not a Palindrome")
