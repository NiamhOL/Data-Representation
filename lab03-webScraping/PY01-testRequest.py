# Test Request

import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

print(page)                 # This will return response 200 
print("------------")
print(page.content)         # This will print the content of the html page 
soup1 = BeautifulSoup(page.content, 'html.parser')      # Improves the format 
print("------------")
print(soup1.prettify())