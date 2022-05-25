import sqlite3

conn = sqlite3.connect("homework1.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')
conn.commit()
spisok = ["slovo", 1, "neslovo", 2, 3]
for i in spisok:
    if i is str:
        cursor.execute('''INSERT INTO tab_1(col_1) VALUES (?)''', (i, ))
        word = len(i)
        cursor.execute('''INSERT INTO tab_2(col_1) VALUES (?)''', (word, ))
    elif i is int:
        if i % 2 == 0:
            cursor.execute('''INSERT INTO tab_2(col_1) VALUES (?)''', i)
        else:
            cursor.execute('''INSERT INTO tab_1(col_1) VALUES ("нечётное")''')
conn.commit()
cursor.execute('''SELECT * FROM tab_1''')
one = cursor.fetchall()
cursor.execute('''SELECT * FROM tab_2''')
two = cursor.fetchall()
conn.commit()
if len(one) < len(two):
    cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
else:
    cursor.execute('''UPDATE tab_1 SET col_1 = "hello" WHERE id = 1''')
cursor.execute('''SELECT * FROM tab_1''')
on = cursor.fetchall()
print(on)
cursor.execute('''SELECT * FROM tab_2''')
tw = cursor.fetchall()
print(tw)
conn.commit()
