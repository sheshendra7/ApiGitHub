import requests
import json
import sys


def getgitdata(userId):

    repositoryResponse = requests.get('https://api.github.com/users/'+userId+'/repos')
    if repositoryResponse.status_code != 200:
        raise FileNotFoundError
        sys.exit()  
    jsonReposiotryResponse = json.loads(repositoryResponse.text)

    if len(jsonReposiotryResponse) <= 0:
        print("No repositories created.")

    for repository in jsonReposiotryResponse:

        commitsResponse = requests.get('https://api.github.com/repos/'+userId+'/'+repository['name']+'/commits')
        if commitsResponse.status_code != 200:
            raise FileNotFoundError
            sys.exit()

        if len(jsonCommitsResponse) <=0:
            return "No commits to the repository "+ repository['name']    
        jsonCommitsResponse = json.loads(commitsResponse.text)
        print("Repo:"+repository['name']+" Number of commits:",len(jsonCommitsResponse))

