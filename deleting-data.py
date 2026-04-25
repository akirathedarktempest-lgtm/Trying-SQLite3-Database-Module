import sqlite3

connect=sqlite3.connect("information.db")
cursor=connect.cursor()

cursor.execute("DELETE FROM data WHERE rowid=2")
print("processing...")
cursor.execute("SELECT * FROM data")
print(cursor.fetchall())
"""Fun fact...the data wasn't deleting actually, actually, it was deleting but it was also not deleting. Like using rowid, if you deleted like rowid once and see, it will disappear"
but if you try it again, considering the 3rd to be 2nd, it won't, and if you change to 1, the two will come back and 1 will be deleted...so we need it to commit the change"""
connect.commit()#and if you just want to delete it for temporary, then don't use commit, if you used commit then it will delete permanently
"""Now it will delete it permanently, but the rowid will remain same of all, for example if we commited the change and try rowid 1 to delete which you already did, nothing would happen
because the 2nd rowid isn't changed and became 1st, it will remain 2nd only and you will have to change"""
