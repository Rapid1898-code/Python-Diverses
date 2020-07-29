from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, Float, MetaData
from sqlalchemy import text

engine = create_engine("mysql+pymysql://root:I65faue#ML5#@localhost/sakila?host=localhost?port=3306")
conn = engine.connect()
#tables = engine.table_names()
#print(tables)
#erg = conn.execute("SELECT * FROM actor").fetchall()
#print(erg[2])


meta = MetaData()
students = Table(
    'students', meta,
    Column('id', Integer, primary_key = True),
    Column('name', String(45)),
    Column('lastname', String(45)),
    Column('floatvar', Float),
)
#meta.create_all(engine)

"""
ins = students.insert()
print(ins)
ins = students.insert().values(name = 'Karan')
print(ins)
print(ins.compile().params)
print(students.update())
print(students.delete())
print(students.select())
"""

ins = students.insert().values(name = 'Ravi', lastname = 'Kapoor')
result = conn.execute(ins)
#print(result.inserted_primary_key)
#print(result)
"""
result = conn.execute(students.insert(), [
   {'name':'Rajiv', 'lastname' : 'Khanna'},
   {'name':'Komal','lastname' : 'Bhandari'},
])
"""

#s = students.select()
#result = conn.execute(s)
#for row in result: print(row)

#s = students.select().where(students.c.id > 10)
#result = conn.execute(s)
#for row in result: print (row)

#t = text("SELECT name FROM students")
#result = conn.execute(t)
#for row in result: print(row)

from sqlalchemy.sql import text
t = text("select students.name, students.lastname from students where students.name between :x and :y")
result = conn.execute(t, x = 'A', y = 'L')
for row in result: print(row)



