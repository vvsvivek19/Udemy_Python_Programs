import heapq
L = [11,22,3,14,25,16,17,28,10]
heapq.heapify(L)
def heap_sort(elements):
    sorted_list = []
    length_of_heap = len(L)
    while L != []:
        item = heapq.heappop(L)
        heapq.heappush(sorted_list,item)
    return sorted_list
print(heap_sort(L))
