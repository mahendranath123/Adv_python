
import sqlite3
con= sqlite3.connect("backup.db")
# create table
# con.execute('''CREATE TABLE gfg (Name text, Points int, accuracy Real)''')

# insert records
# con.execute(''' insert into gfg (Name, Points, accuracy) values('count inversion',20,80.5)''')
# con.execute(''' insert into gfg (Name, Points, accuracy) values('akash ',21,90.5)''')

# display records
# print('Name, Points, accuracy from records with accuracy greater than 85')
# cursor = con.execute(''' select * from gfg where accuracy > 85''')
# for i in cursor:
#     print(i[0] + ' ' + str(i[1]) + ' ' + str(i[2]))
# print('')
# print('Name, Accuracy from records with accuracy greater than 85')
# cursor = con.execute('SELECT name, accuracy from gfg where accuracy > 85')
# for i in cursor:
#     print(i[0] + ' ' + str(i[1]))
# print('')
# cursor = con.execute('select * from gfg')

# update
# cursor = con.execute('''select * from gfg''')
# print('Before update')
# for i in cursor:
#     print(i[0] + ' ' + str(i[1]) + ' ' + str(i[2]))
# print('')

# con.execute('''update gfg set Points=Points+5 where Points <= 20''')


# cursor = con.execute('''select * from gfg''')
# print('After update')
# for i in cursor:
#     print(i[0] + ' ' + str(i[1]) + ' ' + str(i[2]))
    
# delete 
print('before delete')
cursor = con.execute('''select * from gfg''')
for i in cursor:
    print(i[0] +'' + str(i[1]) +'' + str(i[2]))
print('')
cursor = con.execute('''delete from gfg where accuracy >90''')
print('After delete')
cursor = con.execute('''select * from gfg''')
for i in cursor:
    print(i[0] +'' + str(i[1]) +'' + str(i[2]))

con.commit() 

con.close()
