numbers = [int(x) for x in input("Enter the numbers separated by spaces").split()]
unique = []
for x in range(len(numbers)):
    if numbers.count(numbers[x]) == 1:
        unique.append(numbers[x])
    else:
        flag = 0
        for y in range(len(unique)):
            if numbers[x] == unique[y]:
                flag = 1
                break
        if flag == 1:
            pass
        else:
            unique.append(numbers[x])
print(unique)
