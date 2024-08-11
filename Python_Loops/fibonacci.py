n = int(input("Enter how many terms you want: "))
term_sum = 0
first = 0
second = 1
print("My Approach")
print(first)
print(second)
for i in range(2,n):
    term_sum = first + second
    first = second
    second = term_sum
    print(term_sum)
print("========================")
print("Sir's approach")
a = 0
b = 1
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
