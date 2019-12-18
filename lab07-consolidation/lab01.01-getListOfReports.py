import requests
import json


#url = "https://reports.sem-o.com/api/v1/documents/static-reports"

'''
Note the url needed to be https not http which was found by entering: http://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View
into the browser and we  can see there are 50 reports, then we use curl http://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View
it gave more information 301 error and there we can see that the document has moved to https
Note if we only want reports for a specific date we add the date to end of url (&Date=>2019-11-10)

'''
url= "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=>2019-11-10"
response = requests.get(url)
data = response.json()

# for loop that will iterate through the array of items and print the resource names

listOfReports = []
# output to console
# print (data)
for item in data["items"]:
    #print(item["ResourceName"])
    listOfReports.append(item["ResourceName"])

# Here we have a call up the server to get the report itself
for ReportName in listOfReports:
    #print(ReportName)
    url ="https://reports.sem-o.com/api/v1/documents/"+ReportName
    print(url)
    response= requests.get(url)
    aReport= response.json()

#other code
#save this to a file
filename = 'allreports.json'
# Writing JSON data
f =  open(filename, 'w')
json.dump(data, f, indent=4)