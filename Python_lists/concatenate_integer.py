num = input("Please Enter all the numbers for separated by space: ").split()
concat = ''
for x in range(len(num)):
    concat = concat + num[x]
print("Number after concatenation is:", concat)
