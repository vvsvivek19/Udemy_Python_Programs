prod_name = input("Enter the product name: ")
price = input("Enter the price of product: ")
if len(prod_name) + len(price) >= 25:
    print(prod_name,price)
else:
    diff = 25 - len(prod_name) - len(price)
    empty = ''
    print(prod_name + empty.ljust(diff,'.') + price)