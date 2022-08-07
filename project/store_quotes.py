import mysql.connector

mydb = mysql.connector.connect(host ='localhost',user='root',password = 'Suresh@8125')

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE quotes")  creating database

# mycursor.execute("SHOW DATABASES")

# for db in mycursor:
#     print(db)


mycursor.execute("CREATE TABLE quote(Quotes TEXT, Author VARCHAR(255), Tags TEXT")

