import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  #user="datarep",  # this is the user name on my mac
  #passwd="password" # for my mac
  database="datarepresentation"
)

cursor = db.cursor()
# This gets just the first one printed out where the ID is 1

sql="select * from student where id = %s"
values = (1,)

cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
  print(x)


'''
# To get all the students we would run the following 

sql="select * from student"
values = (1,)

cursor.execute(sql)
result = cursor.fetchall()
for x in result:
  print(x)

'''