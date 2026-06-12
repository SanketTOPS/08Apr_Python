import pymysql


try:
    db=pymysql.connect(host='localhost',
                   user='root',
                   password='',
                   database='demodb')
    print("Database Connected!")
except Exception as e:
    print(e)

#Table Create
cr=db.cursor()

create_tbl="create table studinfo(id integer primary key auto_increment,name text,city text)"
try:
    cr.execute(create_tbl)
    print("Table created")
except Exception as e:
    print(e)
    
#Insert Data
"""insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('ashok','baroda'),('hitesh','surat'),('nirav','ahmedabad'),('hardik','navsari')"
try:
    cr.execute(insert_data)
    db.commit()
    print("Record Inserted!")
except Exception as e:
    print(e)"""

#Update Data
update_data="update studinfo set name='harsh',city='gandhinagar' where id=3"
try:
    cr.execute(update_data)
    db.commit()
    print("Record Updated!")
except Exception as e:
    print(e)