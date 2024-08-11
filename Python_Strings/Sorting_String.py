name = 'zkjbfwolizndclasiefacnqwlefnkcackn'
sorted_list = sorted(name)
sorted_string = ''
# for x in range(0, len(name)):
#     if name[x] > name[x + 1]:
#         temp = name[x]
#         name[x] = name[x + 1]
#         name[x + 1] = temp
#     elif x == len(name)-1:
#         break

for x in sorted_list:
    sorted_string = sorted_string + x

sorted_string2 = ''.join(sorted_list)
print(sorted_string)
print(sorted_string2)

