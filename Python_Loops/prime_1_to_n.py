n = int(input("Please enter up to what number you want prime = "))

for i in range(1,n):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        print(i, end=', ')