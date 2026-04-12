'''
The API Mimic: Create a dictionary representing a GitHub API response for a repository. 
It should contain nested dictionaries for owner (name, id, avatar_url) and a list of topics.
'''
import json
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


print(json.dumps(github_repo_response, indent=4))
print(f'====================Phase 1 finished=========================')
print(f'\n')
print("===============================================================")
print("===============================Phase 2============================")
'''
1. Defensive Programming: The .get() Chain
2. Iterating Through Nested Lists with Logic
3. The "Deep Update" Strategy
4. Final Mastery Exercise: The "Dynamic Summary"
5. Why this matters for your Career
'''
print(f'Defensive Programming: The .get() Chain')
'''
The Challenge: Try to get the "Twitter Username" from the owner dictionary 
(which doesn't exist in our data).
'''
print(f'1. Defensive Programming: The .get() Chain')
# Twitter_Username=owner['user_name']
# print(Twitter_Username) # give key error 
Twitter_Username=github_repo_response.get('owner',{}).get('twitter','User Don\'t Existed')
print(Twitter_Username)
# update the twiiter key to github repo
github_repo_response.get('owner',{}).update({'twitter2':'ravi@twitter.com'}) # error
github_repo_response['owner'].update({'twitter':'ravi@twitter.com'})

Twitter_Username=github_repo_response.get('owner',{}).get('twitter','User Don\'t Existed')
print(Twitter_Username)
print(github_repo_response.get('owner',{}))
print('++++++++++++++++++++++++++++++++++++++++++++++++++')
print('2. Iterating Through Nested Lists with Logic')
#2 iteration one is dictionary owner ,topics in github_repo_response dictionary
#topics iteration
print(github_repo_response.get('topics',[]))
for topic in github_repo_response.get('topics',[]):
    print(topic)
# for owner in github_repo_response.get('owner',{}):
#     print(owner)
#extracting only the topics that contain the word "ai" from your repository.
ai_topics= [topic for topic in github_repo_response['topics'] if 'ai' in topic]
print(f'Ai related tags:  {ai_topics}')
#extracting only the twiiter accounts from your repository
twitter_accounts=[]
for account in github_repo_response.get('owner',{}).keys():
       if account =='twitter' or account=='twitter2':
            twitter_accounts.append(github_repo_response['owner'].get(account))
print(twitter_accounts)

print('The deep Update startegy')
'''
When you update a nested dictionary, you must be careful not to overwrite the 
entire dictionary when you only meant to change one value.
'''
#Scenario: You want to add a location to the owner dictionary without 
# deleting their login or id.
github_repo_response['owner'].update({'location':'India','bio':'Ai Engineer'})
print(f'Location:\t {github_repo_response.get('owner',{}).get('location','NA')}')
print(f'Bio:\t{github_repo_response.get('owner',{}).get('bio','NA')}')
print("================================================")
def generate_repo_report(api_data):
    name = api_data.get('name', 'Unknown Project')
    owner = api_data.get('owner', {}).get('login', 'Unknown Owner')
    stars = api_data.get('stargazers_count', 0)
    
    print(f"--- REPOSITORY REPORT: {name.upper()} ---")
    print(f"Created by: {owner}")
    print(f"Popularity: {stars} Stars")
    print(f"Tech Stack: {', '.join(api_data.get('topics', []))}")
    print("-" * 40)

# Run the function
generate_repo_report(github_repo_response)
