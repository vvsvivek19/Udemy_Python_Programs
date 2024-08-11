fav1 = input('Please Enter favorites of friend 1 separated by space: ').split()
fav2 = input('Please Enter favorites of friend 2 separated by space: ').split()
min_sum = (len(fav1) - 1) + (len(fav2) - 1)
fav = ''
for x in range(len(fav1)):
    fav2_index = fav2.index(fav1[x])
    if x + fav2_index < min_sum:
        min_sum = x + fav2_index
        fav = fav1[x]
print("min sum: ", min_sum)
print("Both friends can order", fav)
