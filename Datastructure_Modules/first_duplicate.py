import array

arr1 = array.array('i',[10,20,13,14,15,16,17,10,20,13])
flag = 1
for i in range(len(arr1)):
    if i == 0:
        continue
    else:
        for j in range(i):
            if arr1[i] == arr1[j]:
                print("First Duplicate element is",arr1[i])
                flag = 0
                break
    if flag == 0:
        break
if flag == 1:
    print('No Duplicate in this array')
