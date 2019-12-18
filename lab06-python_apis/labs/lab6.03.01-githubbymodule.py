
# Install package: pip install PyGithub
from github import Github
import requests

g = Github("8c0e5202752a9f00b139b7d0f36bd79f75741975")

repo = g.get_repo("datarepresentationstudent/aPrivateOne")
#print(repo.clone_url)

fileInfo =repo.get_contents("test.txt")

urlOfFile = fileInfo.download_url
#print(urlOfFile)

response = requests.get(urlOfFile)
contentoffile = response.text
#print(contentoffile)

# This is basically the old content file with "more stuff" text added
newContents = contentoffile + " more stuff :) \n"
print(newContents)

GitHubResponse = repo.update_file(fileInfo.path, "Updated by prog", newContents, fileInfo.sha)
print(GitHubResponse)