inventory = {"apple":50, "mango":100, "banana":120, "orange":70}
order =  {"apple":10, "mango":12, "banana":15, "orange":5}

def update_inventory(order):
    print('Updating inventory.....')
    for x in inventory:
        inventory[x] = inventory[x] - order[x]
    print(inventory)

update_inventory(order)