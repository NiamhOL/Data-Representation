import requests
import json

apiKey ='187c7e4d9613ddd34f39e1505cae7d3a0e33f91c'
url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne'
filename = 'repo.json'


#We need to give it token as that is the username that we are logging in with and 
#the key is the password basically. We get JSON back and it is put into a file 

response = requests.get(url, auth=('token', apiKey))


repoJSON = response.json()
# print(response.json)

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)



