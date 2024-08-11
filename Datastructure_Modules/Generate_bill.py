from collections import Counter

Price = Counter(Soap=50, Toothpast=25, Shampoo=45.50 , Toothbrush=15.99)
Cart = Counter(Soap=5, Toothpast=1, Shampoo=2 , Toothbrush=3)
Subtotal = Counter(Soap=0, Toothpast=0, Shampoo=0 , Toothbrush=0)

def generate_bill(cart):
    for x in Price:
        Subtotal[x] = Price[x] * Cart[x]
    print('Product      Price  Qty  Subtotal')
    print("------------------------------------")
    for x in Price:
        print(f'{x:10}: {Price[x]:5} X {Cart[x]:2} = {Price[x]*Cart[x]}')
    print("------------------------------------")
    print("Total:",Subtotal.total())
    print("------------------------------------")

generate_bill(Cart)
