
import requests
import json
from xlwt import *


url = "http://127.0.0.1:5000/cars"

response = requests.get(url)
data = response.json()

# Output to console
print(data)

# Output cars individually 
for car in data["cars"]:
    print(car)

# Other code
# Save this to a file
filename = 'cars.json'

if filename:
    # Writing JSON data
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


# Write to excel file
'''
Here we create a new workBook, add a sheet called cars at row 0 we will write in reg into column 0, text make into column 1 etc...
Then you go onto row number 1 (row+=1) by adding 1 to it 
for loop means for each of the cars in that array cars I get the reg attribute out of that car and store that in column 0 
and whatever row we are at, same thing done for the other attributes
Again we increment the row (row+=1) to the next one row 2.
Then this is saved using: w.save('cars.xls')

'''
w = Workbook()
ws = w.add_sheet('cars')
row = 0;
ws.write(row, 0, "reg")
ws.write(row, 1, "make")
ws.write(row, 2, "model")
ws.write(row, 3, "price")
row += 1

for car in data["cars"]:
    ws.write(row, 0, car["reg"])
    ws.write(row, 1, car["make"])
    ws.write(row, 2, car["model"])
    ws.write(row, 3, car["price"])
    row += 1

w.save('cars.xls')