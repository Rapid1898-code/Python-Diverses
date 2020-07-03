import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="I65faue#ML5#")

print(mydb)

#mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE stockdb")
