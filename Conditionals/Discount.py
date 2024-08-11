amount = float(input("Please enter the total amount: "))
discount = 0
if amount <= 1000:
    print("You are eligible for 10% discount")
    discount = 10
elif amount > 1000 and amount <= 5000:
    print("You are eligible for 20% discount")
    discount = 20
elif amount > 5000 and amount <= 10000:
    print("You are eligible for 30% discount")
    discount = 30
elif amount > 1000:
    print("You are eligible for 50% discount")
    discount = 50
else:
    print("Invalid!!! Please enter valid amount")

amount = amount - ((amount * discount)/100)
print("Total amount after discount is:", amount)