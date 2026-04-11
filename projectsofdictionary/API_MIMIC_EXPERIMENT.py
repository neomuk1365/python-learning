'''
The API Mimic: Create a dictionary representing a GitHub API response for a repository. 
It should contain nested dictionaries for owner (name, id, avatar_url) and a list of topics.
'''
# This is a mock GitHub API response for your Aura project
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
#storing all key in alist
print(f'Learning the structure')
response_keylist=[]
for key in github_repo_response.keys():
    response_keylist.append(key)
    # print(type(key)) # string type
for item in response_keylist:
    print(type(item)) #string type
    # print(item)
#now check for values of dictionary
#value can be single value or dictionary or list 

print('why the type of value is tuple bcz dictionary item() return (key,value) and it\'s type is tuple')
#create a function that check value of which data type-int,str,dict,
# def f(value_list):
#     #using isinstance() to check the type of data type of value
#     # takes 2 argument one is object , another as class/subclass or tuple()
#     if isinstance(value,dict):
#         return "Dictionary"
#     elif isinstance(value , list):
#         return "list"
#     elif isinstance(value, (int,str,float,bool)) or value is None:
#         return "single value"
#     else:
#         return 'other'

# print(help(isinstance))
print(f'===================production way of thinking===============')
def f(data_dict,value):
    # if value not in data_dict:
    #     return "Key Not found"
    if isinstance(value,dict):
        return 'Dictionary'
    elif isinstance(value,list):
        return "list"
    elif isinstance( value, (int,float,str,bool)) or value is None:
        return "Single Value"
    else:
        return "other"

# returning error
'''
 print(f(github_repo_response,value))
          ~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
if value not in data_dict:
       ^^^^^^^^^^^^^^^^^^^^^^
TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict') 
'''
'''
This is not allowed always use key to get value
'''
def f(data_type_dict,key):
    if key not in data_type_dict:
        return "Key Not found"
    value= data_type_dict.get(key)
    if isinstance(value,dict):
        return "dictionary"
    elif isinstance(value,list):
        return "list"
    elif isinstance (value, (int,float,str,bool)) or value is None:
        return "Single Value"
    else:
        return "other"
value_list=[]
print("===================checking value of github repo response=================")
for key,value in github_repo_response.items():
    print(f(github_repo_response,key))
    print(value)
print('my confusion got resolved ')