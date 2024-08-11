import heapq
L = [11,22,3,14,25,16,17,28,10]
heapq.heapify(L)
def Kth_largest(number):
    sorted_list = []
    while L != []:
        item = heapq.heappop(L)
        sorted_list.append(item)
    return sorted_list[len(sorted_list)-number]

num = int(input("Enter the Kth largest number you want to know: "))
if num == 1:
    print(f"{num}st largest number is {Kth_largest(num)}")
elif num == 2:
    print(f"{num}nd largest number is {Kth_largest(num)}")
elif num == 3:
    print(f"{num}rd largest number is {Kth_largest(num)}")
else:
    print(f"{num}th largest number is {Kth_largest(num)}")

