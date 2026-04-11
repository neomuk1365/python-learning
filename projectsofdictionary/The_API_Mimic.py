'''
The API Mimic: Create a dictionary representing a GitHub API response for a repository. 
It should contain nested dictionaries for owner (name, id, avatar_url) and a list of topics.
'''
# This is a mock GitHub API response for our Aura project
github_repo_response = {
    "id": 87654321,
    "name": "Aura-AI-Life-Assistant",
    "full_name": "raviranjan/Aura-AI-Life-Assistant",
    "private": False,
    "owner": {
        "login": "raviranjan",
        "id": 1234567,
        "avatar_url": "https://github.com/images/error/ravi_happy.gif",
        "type": "User",
        "site_admin": False
    },
    "description": "Unified AI Life-Load Assistant that brideg gap between personal and professional task",
    "html_url": "NA",
    "stargazers_count": 42,
    "topics": [
        "python", 
        "ai-assistant", 
        "ml-engineering", 
        "stream-lit", 
        "hackathon"
    ],
    "visibility": "public",
    "forks": 10
}
# performing 4 operation on this data 1 .get(),manupulating,updating, reports

print('Access Nested value safely')
#in production we never know key exist so we will use .get()
print('accesing owner id i.e it is dictionary inside dictionary')
print(github_repo_response.get('owner',{}))
print(github_repo_response.get("owner",{}).get('id','NA'))
print(github_repo_response.get('owner',{}).get('login','SignUp First!'))
useravailable=github_repo_response.get('owner',{}).get('user','NA')
typeofuser=github_repo_response.get('owner',{}).get('type','NA')
print(f'{useravailable}\n{typeofuser}')

#Manipulate the nested list
print(f'Manipulating Nested dictionary')
#here github_repo_response dictionary and owner is dictionary inside dictionary 
# github_repo_response
# "owner": {
#         "login": "raviranjan",
#         "id": 1234567,
#         "avatar_url": "https://github.com/images/error/ravi_happy.gif",
#         "type": "User",
#         "site_admin": False
#     }
#chnage the login :'jitendarlenka',id:'7654321',avatar_url:'https://solvelife.streamlit.app/',
#           type :'admin_user',site-admin:'True'
# to acces this we will use [] github_repo_response.get('login')
github_repo_response['owner']['login']='jitendarlenka'
github_repo_response['owner']['id']=7654321
github_repo_response['owner']['avatar_url']='https://solvelife.streamlit.app/'
github_repo_response['owner']['type']='admin_user'
github_repo_response['owner']['site-admin']='True'
for key, value in github_repo_response['owner'].items():
    print(f'{key}\t{value}')
#updating the list in this dictionary and priting it's value
print('Updating the lists i.e. inside the dictionary')
print('topics list inside disctionary')
print(github_repo_response.get('topics',[]))
#accesing this 
# print(github_repo_response['topics'][0])
for topic in github_repo_response.get('topics',[]):
    print(topic)
#update topics to 'nlp'
github_repo_response['topics'].append('nlp')
github_repo_response['topics'].append('dictionary')
print('topics list after updating 2 value in topics list')
print(github_repo_response['topics'])
print("======================================================================")

import json
print(json.dumps(github_repo_response, indent=4))
print(f'====================Phase 1 finished=========================')
print(f'\n')
