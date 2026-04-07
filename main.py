import sqlite3

connect=sqlite3.connect("information.db")
cursor=connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS data(
               user text,
               user_global_name text,
               user_id integer,
               info_submitted text)""")

def storedata():
    u=input("User: ")
    ugn=input("Username commonly known: ")
    uid=input("User ID: ")
    ins=input("Info: ")
    d={"user":u,"user_global_name":ugn,"user_id":uid,"info_submitted":ins}
    return d

info=storedata()
print(info)#this was...because I wasn't sure whether it will work or not so I was using print, you can remove that
l=[info["user"],info["user_global_name"],info["user_id"],info["info_submitted"]]
print(l)#same, lack of confidence...can't help :(
cursor.execute("INSERT INTO data (user,user_global_name,user_id,info_submitted) VALUES (?,?,?,?)",l)
connect.commit()
cursor.execute("SELECT * FROM data")
print(cursor.fetchall())#...don't need to explain
connect.close()
