fav_food = input("Please enter all the favorite foods separated by space: ").split()
letter = input('Input a letter you want to search: ')
letter = letter.lower()
for x in fav_food:
    if x.startswith(letter):
        print("Word found!!! Your food is",x)
