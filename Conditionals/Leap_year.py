year = int(input("Please enter a year: "))

if year % 100 == 0: #this if is for checking years multiple of 100 and 400
    if year % 400 == 0:
        print("It is a leap year!")
    else:
        print("Not a leap year!")
elif year % 4 == 0: #To check for years which are not multiples of 100 or 400
    print("It is a leap year!")
else:
    print("Not a leap year!")
