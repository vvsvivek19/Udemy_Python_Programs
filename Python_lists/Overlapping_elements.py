l1= [int(x) for x in input("please enter all the elements separated by space: ").split()]
l2= [int(y) for y in input("please enter all the elements separated by space: ").split()]
l3 = []
for x in l1:
    if x not in l3:
        if x in l2:
            if x in l3:
                pass
            else:
                l3.append(x)
print(l3)