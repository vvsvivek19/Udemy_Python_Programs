user_string = input("Please enter a string: ")
reverse_string = user_string[-1::-1]
if user_string == reverse_string:
    print("Reverse String:", reverse_string)
    print("String is Palindrome")
else:
    print("Reverse String:", reverse_string)
    print("Not a palindrome")
