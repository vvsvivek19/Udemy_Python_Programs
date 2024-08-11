john = float(input("Enter the age of John: "))
smith = float(input("Enter the age of Smith: "))
ajay = float(input("Enter the age of Ajay: "))

# if john > smith and john > ajay:
#     print("John is eldest!")
# else:
#     if smith > ajay:
#         print("Smith is eldest!")
#     else:
#         print("Ajay is eldest!")

if john > smith and john > ajay:
    print("John is eldest!")
elif smith > ajay:
    print("Smith is eldest!")
else:
    print("Ajay is eldest!")