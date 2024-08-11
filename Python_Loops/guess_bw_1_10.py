import random
n = random.randint(1,20)
num = int(input("Guess the number between 1 to 20: "))
counter = 1
upper_limit = 20
lower_limit = 0
while counter != 0:
    if num > n:
        upper_limit = num
        print("Wrong!!! A New Upper limit has been set")
        print("Please guess between", lower_limit, "and", upper_limit)
        num = int(input("Guess the number between 1 to 20: "))
    elif num < n:
        lower_limit = num
        print("Wrong!!! A New lower limit has been set")
        print("Please guess between", lower_limit, "and", upper_limit)
        num = int(input("Guess the number between 1 to 20: "))
    else:
        print("Congrats!! you guessed it right")
        print("Random number:", n)
        counter = 0