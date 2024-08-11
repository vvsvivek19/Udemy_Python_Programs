import sqlite3

conn = sqlite3.connect("shop.db")

cur = conn.cursor()

flag = 1

while flag == 1:
    OrderNo = int(input('Enter Order Number: '))
    Custid = input('Enter Customer ID: ')
    ProdNo = input('Enter Product Number: ')
    Qty = int(input('Enter Quantity: '))
    cur.execute(f'''INSERT INTO "Order" VALUES({OrderNo},'{Custid}','{ProdNo}',{Qty})''')
    prompt = input('Want to Enter more? Y or N: ')
    if prompt.lower() == 'y':
        pass
    else:
        flag = 0

conn.commit()

cur.close()

conn.close()