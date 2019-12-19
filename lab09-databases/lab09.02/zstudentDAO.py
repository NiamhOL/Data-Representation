import mysql.connector

# Note by convention classes begin with a capital letter. 
class StudentDAO:
    db=""                                           # Here we make a variable db which is blank at the moment 
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="datarepresentation"
        )
    
# Create: the cursor is to get the database from this class and then do the insert. 
# Note it is the values that is passed into the function!
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into student (name, age) values (%s,%s)"
        cursor.execute(sql, values)
# Note here we return the ID of the last one created 
        self.db.commit()
        return cursor.lastrowid

# getAll this basically gets all and returns back the array 
    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from student"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

# findByID we pass in the ID and make a tuple with the ID when executed the %s will become the ID 
    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from student where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return result

# Update: cursor updates self students for the tuple (name equals the first entry, age is second and ID is the third) 
    def update(self, values):
        cursor = self.db.cursor()
        sql="update student set name= %s, age=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
 
# delete justs takes in the ID and deletes that
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from student where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

# Makes a new instance of the studentDAO so when I am testing it 
studentDAO = StudentDAO()