class Orders:
    def __init__(self):
        self.cart = []
    def add_to_cart(self,item):
        self.cart.append(item)
    def remove_from_cart(self,item):
        self.cart.remove(item)
        print('One item removed')
    def __len__(self):
        count = 0
        for item in self.cart:
            count += 1
        return count
    def __str__(self):
        items = 'Card Contents: '
        count = 1
        if self.cart == []:
            print('No items in list, please add items. \n*************************')
            return items
        else:
            for item in self.cart:
                items = items + '\n' + str(count) + '. ' + str(item)
                count += 1
        return items

choice = int(input('=======================================\nPlease select what you want to do:\n1. Add item to cart\n2. Remove item from cart \n3. View items in Orders\n4. Exit\nEnter your choice here out of 1 to 4: '))
o = Orders()
while choice != 4:
    match choice:
        case 1:
            item_name = input('Please Enter Item name to add:')
            o.add_to_cart(item_name)
        case 2:
            try:
                item_name = input('Please Enter Item name to remove: ')
                o.remove_from_cart(item_name)
            except ValueError as m:
                print('No Such item in the cart. ')
                choice = int(input('=======================================\nPlease select what you want to do:\n1. Add item to cart\n2. Remove item from cart \n3. View items in Orders\n4. Exit\nEnter your choice here out of 1 to 4: '))
        case 3:
            print('Total items in order:', len(o))
            print('*'*40)
            print(o)
    choice = int(input('=======================================\nPlease select what you want to do:\n1. Add item to cart\n2. Remove item from cart \n3. View items in Orders\n4. Exit\nEnter your choice here out of 1 to 4: '))
    if choice == 4:
        print('Bye Bye! I hope we will see you again')

# o.add_to_cart('Diet Coke')
# o.add_to_cart('Lays Chips')
# o.add_to_cart('Smartphone')
# print('Total items in order:',len(o))
# print(o)
# o.remove_from_cart('Smartphone')
# print('Total items in order:',len(o))
# print(o)

