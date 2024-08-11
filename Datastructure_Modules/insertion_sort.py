import bisect


L = [2,4,6,8,10,3,5,1,7,9]

def insertion_sort(elements):
    sorted_list = []
    for e in elements:
        bisect.insort(sorted_list,e)
        print(sorted_list)
    return sorted_list

print(insertion_sort(L))