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
    l=[d["user"],d["user_global_name"],d["user_id"],d["info_submitted"]]
    cursor.execute("INSERT INTO data (user,user_global_name,user_id,info_submitted) VALUES (?,?,?,?)",l)
    connect.commit()

storedata()
cursor.execute("SELECT * FROM data")
print(cursor.fetchall())
"""Now what happened here? So basically, this was a shorter form to do everything. As we know, functions are use to not reuse the same code, in the last time, we just used once, but what if we use it more times?
We will basically take the return, make the function a variable, take and then make a list again, we are doing same things so it's better to inclue it already in the function to not reuse like that.
Now we can do this now"""
storedata()#we can do it many times, no need to make it a list and all that
storedata()#once again
connect.close()#this is a good habit :thumbsup:
#and one more thing...i just now noticed that Github tab takes two spaces while in VS code it's four, so maybe check it if the indentation is wrong in your code...do it on your own
