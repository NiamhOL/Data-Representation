 # Here is the test code so from the zstudentDAO  we import the studentDAO instance of the class that means 
 # when we create I can call the studentDAO.Create and pass in the tuple of those values.
from zstudentDAO import studentDAO

#create
latestid = studentDAO.create(('mark', 45))


# find by id: I just pass in the ID I want to find which is the latest one we got back 
result = studentDAO.findByID(latestid);
print (result)

# update: here we pass in the tuple we want to create the last entry in the tuple one again is the lastID 
# and then we do a findbyID again to see if it is the same 
studentDAO.update(('Fred',21,latestid))
result = studentDAO.findByID(latestid);
print (result)

# get all: All students refers to getAll in this case it passes back the array of all students
allStudents = studentDAO.getAll()
for student in allStudents:
  print(student)

# delete the last id created 
studentDAO.delete(latestid)