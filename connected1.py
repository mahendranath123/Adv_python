import sqlite3
con=sqlite3.connect('..test.db1')
cur=con.cursor()
qry='''
    create table employee1(
        emp integer primary key,
        first_name varchar(20),
        last_name varchar(20),
        age int,
        sex text(1),
        income float);
'''                                                                            
try:
    cur.execute(qry)
    print("table is created")
except:
    print("error creating table")
         
 
# qry=''' show tables'''
# cur.execute(qry)
con.close()

