try:
    n = int(input("How many numbers you want to enter?: "))
    if n > 0:
        max = int(input("Enter a number: "))
        while n != 1:
            num = int(input("Enter a number: "))
            if num > max:
                max = num
            n -= 1
        print("Maximum number entered was:", max)
    else:
        print("Please enter a positive number!!")
except Exception as e:
    print("Invalid Input!! Please Enter a valid input. Error:", e)
