import random
import sqlite3

conn = sqlite3.connect("homework2.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT,
col_1 INTEGER, col_2 INTEGER)''')
number_1 = random.randint(0, 9)
number_2 = random.randint(0, 9)
cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES (?, ?)''', (number_1, number_2))
conn.commit()
cursor.execute('''SELECT col_1 FROM tab_1''')
k = cursor.fetchall()
cursor.execute('''SELECT col_2 FROM tab_1''')
d = cursor.fetchall()
print(k)
print(d)
l = list(zip(k, d))
print(l)
spisok = []
for i in l:
    s = 0
    for j in range(len(l)):
        s += l[i]
print(spisok)