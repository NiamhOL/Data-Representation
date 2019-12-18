import requests
import json

# html = '<h1>hello world</h1>This is html'
'''
This program takes in a file carviewer2.html from week 2, this is read in and stored
as text html
api key taken from website which is sent to your email address 
url we go to when looing at the documentation 

'''
f = open("../../lab02-JS/carviewer2.html", "r")
html = f.read()
# print (html)

apiKey = '46ceed910c24ff7cce8240e89ec7b71912f6f40f2ec55fd217ce150ad6d4f1c4'
url = 'https://api.html2pdf.app/v1/generate'

data = {'html': html,'apiKey': apiKey}
response = requests.post(url, json=data)
print (response.status_code)
'''
opens up a new file and I will write that back out. Note the new file is a pdf file 
we take the content which is binary status code printed just so we know it works 

'''
newFile = open("lab06.02.01.htmlaspdf.pdf", "wb")
newFile.write(response.content)