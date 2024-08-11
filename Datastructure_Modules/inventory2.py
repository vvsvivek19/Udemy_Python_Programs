from collections import Counter
# inventory = {"apple":50, "mango":100, "banana":120, "orange":70}
# order =  {"apple":10, "mango":12, "banana":15, "orange":5}
#
# inventory_counter = Counter(inventory)
# order_counter = Counter(order)
# inventory_counter.subtract(order_counter)
# print(inventory_counter)

inventory = Counter(apple=50,mango=100,banana=120,orange=70)


def update_inventory(order):
    inventory.subtract(order)

order = Counter(apple=10,banana=12,orange=5)

update_inventory(order)
print(inventory)