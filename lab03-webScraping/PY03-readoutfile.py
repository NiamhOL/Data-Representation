  
from bs4 import BeautifulSoup
 
with open("../lab02-JS/carviewer2.html") as fp:
   soup = BeautifulSoup(fp, 'html.parser')
 

# print(soup.tr)      #  This prints out the first element that has the tr tag

# Below the code will go through all the tr tags and print them out
rows = soup.findAll("tr")
for row in rows:
    #print(row)
    datalist = []
    cols = row.findAll("td")            # this will find all the td tags
    for col in cols:
        datalist.append(col.text)
    print(datalist)

 