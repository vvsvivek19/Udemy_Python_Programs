import array

arr1 = array.array('i',[1, 2, 4, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19, 21, 22, 23, 25, 26, 27, 29, 30, 31, 33, 34, 35, 37, 38, 39, 41, 42, 43, 45, 46, 47, 49, 50, 51, 53, 54, 55, 57, 58, 59, 61, 62, 63, 65, 66, 67, 69, 70, 71, 73, 74, 75, 77, 78, 79, 81, 82, 83, 85, 86, 87, 89, 90, 91, 93, 94, 95, 97, 98, 99, 101, 102, 103, 105, 106, 107, 109, 110, 111, 113, 114, 115, 117, 118, 119, 121, 122, 123, 125, 126, 127, 129, 130, 131, 133, 134, 135, 137, 138, 139, 141, 142, 143, 145, 146, 147, 149, 150])

for i in range(len(arr1)):
    if i == 0:
        continue
    else:
        if arr1[i-1] - arr1[i] == -1:
            continue
        else:
            diff = arr1[i] - arr1[i-1]
            x = 1
            for j in range(diff-1):
                print(arr1[i] - x)
                x += 1

