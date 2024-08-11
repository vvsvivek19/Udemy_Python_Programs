flag = 0
while flag != 1:
    pass1 = input("Pleas Enter a password: ")
    pass2 = input("Reconfirm your password: ")
    if pass1 == pass2:
        print("Good! Passwords match.")
        flag = 1
    elif pass1.casefold() == pass2.casefold():
        print("There is some mismatch in password's case. Please re-enter the password with same cases")
        flag = 0
        continue
    else:
        print("Password don't match")
        flag = 0
        continue
