import array

arr = array.array('i',[0,-1,-3,-5,-8,2,4])
highest = 0
prod = 0
first = 0
second = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[j] == arr[i]:
            continue
        prod = arr[i] * arr[j]
        if prod > highest:
            highest = prod
            first = arr[i]
            second = arr[j]
print('Highest Product:',highest)
print(f'Highest Pair ({first},{second})')