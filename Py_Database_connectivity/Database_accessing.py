import sqlite3

conn = sqlite3.connect("univ.db")
cur = conn.cursor()

rows = cur.execute('DELETE FROM Dept WHERE deptno = 40')

conn.commit()

# allrows = rows.fetchall()
# print('Names are: ')
# for t in allrows:
#     print(t[0],t[1])

cur.close()

conn.close()