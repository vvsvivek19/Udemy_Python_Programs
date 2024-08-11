a = int(input("Enter the first time =  "))
d = int(input("Enter the common difference =  "))
n = int(input("Enter the total number of terms = "))
print("Your Arithmetic series is: ")
for i in range(0,n):
    term = a + (i * d)
    print(term)