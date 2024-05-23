import sqlite3;
con=sqlite3.connect('pr1.db')
# con.execute(''' create table pr1  (id integer , name varchar(50)) ''')
# con.execute('''insert into pr1 (name,id) values ('akash',1) ''')
# con.execute('''insert into pr1 (name,id) values ('akash',2) ''')
# con.execute('''insert into pr1 (name,id) values ('akash',3) ''')
# cursor=con.execute('''   select * from pr1 ''')
# for i in cursor:
#     print(i[0],i[1])
cursor=con.execute(''' select * from pr1 where id =2 ''')
for i in cursor:
    print(i[0] + (i[1]))
print(' ')
con.commit()
con.close()
