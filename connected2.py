import sqlite3 
con =sqlite3.connect("test.db1")
cur=con.cursor()
qry= ''' insert into employee1(emp,first_name ,last_name ,age,sex, income)
 values(101,'ankush', 'Kumar', 25, 'M', 10000)'''
try:
    cur.execute(qry)
    con.commit()
    print("Record inserted successfully")
except : 
    con.rollback()
    print("error in insert operation")
con.close()
    