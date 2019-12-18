import requests
import json
from xlwt import *

'''
When this code is run it makes a file called allReports. If there is more than
50 reports being returned back then it returns it back in pages so there is a page 
size of 50 current page is 1 and the total pages is 14. Thus to get the next page 
copy and paste the url into browser (&page=2) would be added to end of url to give you
page number 2. In this script we need to get the total number of pages and iterate through them 
using a while loop

'''

#url = "https://reports.sem-o.com/api/v1/documents/static-reports"

# Please note we have taken off the end which dealt with the date: seen in  lab01.02-getReportData.py
url= "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View"
response = requests.get(url)
data = response.json()
totalPages = data["pagination"]["totalPages"]         # This allows us to find the total number of pages 
#print (totalPages)
listOfReports = []

# Here we have a while loop that iterates through all the pages starting at page number 1
pageNumber=1
while pageNumber <= totalPages:
    pageUrl = url + "&page="+ str(pageNumber)
    #print (pageUrl)

    data = requests.get(pageUrl).json()
    
 # Here we put data items into a list .
    
    for item in data["items"]:
        #print(item["ResourceName"])
        listOfReports.append(item["ResourceName"])

    pageNumber +=1

#output to console
#print (data)

# for loop used to output all the report names
for reportName in listOfReports:
    print(reportName)

filename = "allReports.json"
f =  open(filename, 'w')
json.dump(data, f, indent=4)