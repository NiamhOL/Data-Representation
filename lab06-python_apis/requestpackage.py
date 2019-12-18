'''
Creates a simple request up to the gmit website 

'''

import requests

'''
Variable called url with the website gmit 

'''
# url = "https://www.gmit.ie"

# response = requests.get(url)            
# print(response.status_code)                # when printed we got a status of 200 everything is fine 
# print(response.text)                       # prints out all the html that we get from gmit website 
# print(response.headers)                    # this will get the headers from 

'''
Below we will do a post using the restserver API that was used last week.
Instead of using gmit website above we will use  the url below. 
Here we are sending something up to cars 
data is a dict object and that will automatically get converted into JSON by the requests package 
'''
url = 'http://127.0.0.1:5000/cars'
data = {'reg':'123', 'make':'blah', 'model':'blah', 'price':1234}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())