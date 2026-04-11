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
# performing 4 operation on this data
print('Access Nested value safely')
#in production we never know key exist so we will use .get()
print('accesing owner id i.e it is dictionary inside dictionary')
print(github_repo_response.get('owner',{}))
print(github_repo_response.get("owner",{}).get('id','NA'))
print(github_repo_response.get('owner',{}).get('login','SignUp First!'))
typeofuser=github_repo_response.get('owner',{}).get('user','NA')
