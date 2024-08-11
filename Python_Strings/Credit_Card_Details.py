credit_card_num = input("Please enter your credit card details")
last_digits = credit_card_num[14:len(credit_card_num):1]
print("Credit card details are: " + "**** " * 3 + last_digits)