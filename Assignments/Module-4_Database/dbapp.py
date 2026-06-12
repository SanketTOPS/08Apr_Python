import sqlite3

db=sqlite3.connect("tops.db")
print("Database created/connected")

#Table Create
create_tbl="create table studinfo(id integer primary key autoincrement,name text,city text)"
try:
    db.execute(create_tbl)
    print("Table created")
except Exception as e:
    print(e)

#Insert Data
"""insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('ashok','baroda'),('hitesh','surat'),('nirav','ahmedabad'),('hardik','navsari')"
try:
    db.execute(insert_data)
    db.commit()
    print("Record Inserted!")
except Exception as e:
    print(e)"""

#Update Data
"""update_data="update studinfo set name='harsh',city='gandhinagar' where id=3"
try:
    db.execute(update_data)
    db.commit()
    print("Record Updated!")
except Exception as e:
    print(e)"""

#Delete Data
"""delete_data="delete from studinfo where id=5"
try:
    db.execute(delete_data)
    db.commit()
    print("Record Deleted!")
except Exception as e:
    print(e)"""
    
#Show Data
cr=db.cursor()
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    dt=cr.fetchall()
    #dt=cr.fetchmany(3)
    #dt=cr.fetchone()
    #print(dt)
    
    for i in dt:
        print(i)
except Exception as e:
    print(e)
    