from bs4 import BeautifulSoup
 
with open("../lab02-JS/carviewer2.html") as fp:
   soup = BeautifulSoup(fp, 'html.parser')
 
print(soup.prettify())