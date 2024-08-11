import array

def find_duplicate(nums):
    num_set = set()

    for n in nums:
        if n in num_set:
            return n
        else:
            num_set.add(n)
    else:
        return -1

arr1 = array.array('i',[10,20,13,14,15,16,17,10,20,13])
print(find_duplicate(arr1))