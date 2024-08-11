L = [307640, 10, 200000, 56,78,98,34,50 ,70,12,565,689,90,1000,325,54634,80,2345,1123240,342356325]
def sum_zero(Array):
    sum = 0
    for i in L:
        if i%10 == 0:
            sum += i
    return sum


print("Sum of numbers ending with zero is:", sum_zero(L))