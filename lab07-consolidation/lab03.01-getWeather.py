import requests
import json

dateToSearch="2019-11-10"
# I decided to look at yesterday weather instead of today 
url= "https://prodapi.metweb.ie/observations/newport-furnace/yesterday"
response = requests.get(url)
data = response.json()
print(data)

for row in data:
    print (row["pressure"])
#filename = "weatherReport.json"
# Writing JSON data
#f =  open(filename, 'w')
#json.dump(data, f, indent=4)

