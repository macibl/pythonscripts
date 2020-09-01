#!/usr/bin/env python
# use_requests : use of REST API library "requests"
# with GitHub REST API url 

import requests         # see https://requests.readthedocs.io/en/master/
import os
from pprint import pprint
import json             # see https://docs.python.org/3/library/json.html

# see https://developer.atlassian.com/cloud/confluence/rest-api-examples/
# print correctly response from a requests.get() 
#def printResponse(r):
#    print '{} {}\n'.format(json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': ')), r)
    
    
res = requests.get('https://api.github.com/events')
# r.text
#print('https://api.github.com/events:', res)                  # print only response status code : <Response [200]>
#print('https://api.github.com/events in text:', res.text)     # print all json on one line
#print('https://api.github.com/events in json:', res.json)     # print only  <bound method Response.json of <Response [200]>>


# Access to info of a user's repositories in https://api.github.com/users/{owner}/repos
# maybe also : access to an authenticated user repositories with https://api.github.com/user/repos 
# see REST API here : https://docs.github.com/en/rest/reference/repos#list-repositories-for-the-authenticated-user
# only those with visibilty = public (see reference doc for available parameters)
# with curl, would be: 
#  curl -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/users/macibl/repos
#
# with use of a personal access token created on github - settings
# token is at minimum in .bashrc as export GITHUB_TOKEN="013456..." 
token = os.getenv('GITHUB_TOKEN', '...')         # default value if GITHUB_TOKEN doesn't exist : '...'
#pprint(token)

owner = "macibl"
query_url = f"https://api.github.com/users/{owner}/repos"
headers = {'Authorization': f'token {token}'}
lookForParams = {
    'visibility': 'public', 'sort': 'updated'
}
r = requests.get(query_url, headers=headers, params=lookForParams)

#pprint(r.text)         # pretty print content even if not json data
                         # better is to use the builtin json decoder:
#pprint(r.json())        # with pretty print, display for each repo all fields in json, one per line  
#pprint(r.json()[1])      # print one element of the list, i.e. here infos for one repo       
#print(r.json())         # with classic print, display for each repo all fields in json on only one line

# print all key-value pairs with a for loop
# response is a list of dictionnaries, then you need to choose one element of the list (a dictionnary) before use .item()
jsonResponse=r.json()[1]
print("Print each key-value pair from JSON response")
for key, value in jsonResponse.items():
    print(key, ":", value)

# TODO : print sub dictionnaries content as key-value pairs, for instance for owner key

print('============================================================')

# access to a user's public information with https://api.github.com/users/{owner}
# see reference for that request here: https://docs.github.com/en/rest/reference/users#get-a-user
# no need of authentification
owner = "macibl"
query_url = f"https://api.github.com/users/{owner}"
r = requests.get(query_url)

jsonResponse=r.json()
print('Pretty print of JSON response for https://api.github.com/users/{owner}')
pprint(jsonResponse)    # same as pprint(r.json())

print()

# print all key-value pairs with a for loop
print("Print each key-value pair from JSON response")
for key, value in jsonResponse.items():
    print(key, ":", value)

print()

# print value for a given key
print("Access directly using a JSON key name")
print("URL is ")
print(jsonResponse["url"])


# check with json.tool: see https://docs.python.org/fr/3/library/json.html
# use: python use_requests.py | python -m json.tool
# TODO : check why there is an error found:
# Expecting property name enclosed in double quotes: line 1 column 3 (char 2)

# TODO use of conditional request with Etag


# TODO: save in a file
#with open('use_requests_file.json', 'w') as fd:
    #for chunk in r.iter_content(chunk_size=128):
#    fd.write(json.dumps(r.json, indent=4))





