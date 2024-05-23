import mysql.connector

# connection to mysql server
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
    
)

#cursor object c
c=db.cursor()

#excecuting the create database statement
c.execute("create database employee1")

# fetching all the database statements

c.execute("show databases")

# printing all the database statements

for x in c():
    print(x)
c=db.cursor()

# Finally closing  the datbase connection
db.close()