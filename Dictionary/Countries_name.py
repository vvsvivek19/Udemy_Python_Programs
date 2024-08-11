name = input("Please Enter All countries name separated by space and start with Capital letter: ").split()
countries = dict()
for x in name:
    if x[0].upper() not in countries:
         countries[x[0].upper()] = [x]
    else:
        countries[x[0].upper()].append(x)
print(countries)