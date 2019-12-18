import json

# Simple dict object that has 3 attributes in it. It is very like JSON except in Python we can have single or double quotes around the  attributes i.e. name, age and student 
data = {
    'name':'joe',
    'age': 21,
    'student': True,

}
# print(data)

# Convert this into JSON

# w allows you to write to the file 
file = open("simple.json", "w")

'''
json dump (what we want to dump (data), into the file(file), indent=4 literally means it will put 4 white spaces and make it look neater ) 
when running the below code uncomment it and  use the following commands:
    python jsonPackage.py            ls          cat simple.json
'''
# json.dump(data, file, indent=4)

'''
 If we don't want to put it into a file (commented out above) and instead want to put it into a JSON string 
Below code means we can  get a string and then pass it up to a server. Note unlike the code above this should come out with double quotes
Note the true for student comes out as a lowercase true because that is what the mapping is in python true has a capital T
'''

jsonString = json.dumps(data)
print(jsonString)
