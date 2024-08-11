numbers = [int(x) for x in input("Enter the numbers separated by spaces").split()]
index = numbers.index(10,0,len(numbers))
print(index)
