year = int(input("Please enter a year: "))

if year % 100 == 0:
    if year % 400 == 0:
        print("It is a leap year!")
    else:
        print("Not a leap year!")
elif year % 4 == 0:
    print("It is a leap year!")
else:
    print("Not a leap year!")
