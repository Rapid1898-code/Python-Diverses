import mysql.connector

mydb = mysql.connector.connect\
    (host="localhost",user="root",passwd="I65faue#ML5#",database="stockdb")
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE stockdb")

#mycursor.execute("SHOW DATABASES")
#for db in mycursor: print(db)

#mycursor.execute("CREATE TABLE students (name VARCHAR(255),age INTEGER(10))")

#mycursor.execute("SHOW TABLES")
#for tb in mycursor: print(tb)

#sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
#students = [("Rachel", 22),("Mark", 29),("Clara", 52),("Stefan", 19),("Helmut", 34)]
#mycursor.executemany(sqlFormula,students)
#mydb.commit()

sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
students = [("Rachel", 22)]
mycursor.executemany(sql,students)
mydb.commit()

#sql = "UPDATE students SET age = 82 WHERE name='Helmut'"
#sql = "SELECT * FROM students LIMIT 5"
#sql = "SELECT * FROM students ORDER BY name DESC"
#sql = "SELECT * FROM students LIMIT 5 OFFSET 5"

# sql = "DELETE FROM students WHERE age>10"
# mycursor.execute((sql))
# mydb.commit()

#myresult = mycursor.fetchall()
#print(myresult)
#for row in myresult: print(row)






