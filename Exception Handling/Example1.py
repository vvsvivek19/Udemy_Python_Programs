L = [10, 20, 30, 40, 50]
try:
    index = int(input("Please Enter a index: "))
    print(L[index])
    print("End of try block")
except (IndexError, ValueError) as msg:
    print('Error Message:', msg)
except:
    print("Some Error Occurred!")
print("Terminated gracefully")
