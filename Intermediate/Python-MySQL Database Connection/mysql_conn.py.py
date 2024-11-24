import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rahul@0603"
)
print(mydb)

mycursor =  mydb.cursor()
mycursor.execute("CREATE DATABASE LIBRARY1")
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)


mycursor.execute("USE LIBRARY1")
mycursor.execute("CREATE TABLE FICTION(Bookid int primary key AUTO_INCREMENT , BookName varchar(30) NOT NULL , Price decimal(6,2))")
mycursor.execute("INSERT INTO FICTION VALUES(1, 'Avengers-Infinity Saga', 899)")
mydb.commit()
