import sqlite3

connect=sqlite3.connect("information.db")
cursor=connect.cursor()
cursor.execute("SELECT * FROM data")
print(cursor.fetchall())
#and this is to see the database seperately, I forgot to show in better_way.py so this will just run to show the database data
