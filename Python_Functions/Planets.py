def planet_name(id):
    if id >= 1 and id <= 9:
        planets = {1: 'Mercury',
                   2: 'Venus',
                   3: 'Earth',
                   4: 'Mars',
                   5: 'Jupiter',
                   6: 'Saturn',
                   7: 'Uranus',
                   8: 'Neptune',
                   9: 'Pluto'}
        print("Your chosen planet is", planets[id])
    else:
        print("Bitch, Please Enter a Valid Planet number!")


ID = int(input("Please Enter a Number between 1 to 9: "))
planet_name(ID)
