import math
a = float(input("Enter the value of A: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of C: "))
root1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
root2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
print("Roots are: ", root1, root2)
