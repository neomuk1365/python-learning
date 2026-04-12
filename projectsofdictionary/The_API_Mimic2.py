raw_logs=[
    {'user':'Ravi','task':'Data Cleaning','hours':4,'status':'Done'},
    {'user':'Jake','task':'Model Training','hours':5,'status':'Done'},
    {'user':'Ravi','task':'Api Integeration','hours':3,'status':'Done'},
    {'user':'Marty','task':'UI Design','hours':4,'status':'Done'},
    {'user':'Jake','task':'Testing & Manual Testing','hours':6,'status':'Done'},
    {'user':'Marty','task':'Backend Design','hours':8,'status':'Done'}
]
'''
{
'Ravi':
{
'tasks':['Data Cleaning','Api Integeration'],
'total_hours':7,
'completion_rate':100.0
},
'Jake':{
'tasks':['Model Training','Testing & Manual Testing'],
'total_hours':11,
'completion_rate':100.0
},
'Marty':{
'tasks':['UI Design','Backend Design'],
'total_hours':12,
'completion_rate':100.0
}
}
'''
nested_dictionary={}
for log in raw_logs:
    #log is dictionary and i have to use (user,value) value as my nested nested_dictionary key 
    user=log.get('user','NA')
    if user not in nested_dictionary.keys():
        nested_dictionary={
            user:{

            'tasks':[],
            'total_hours':0.0,
            'completion_rate':0
            },
        }
#only printing the last log of the raw_logs
print(nested_dictionary)
print("=================================")
nested_dict={}
for log in raw_logs:
    user=log.get('user')
    if user not in nested_dict:
        nested_dict[user]={
            'tasks':[],
            'total_hours':0,
            'completed_tasks':0,
            'total_tasks':0
        }
    #Try modifying: Only include tasks where status == "Done"
    if log['status']=='Done':
        nested_dict[user]['tasks'].append(log['task'])
        nested_dict[user]['total_hours']+=log['hours']
        nested_dict[user]['total_tasks']+=1
    if log['status']=='Done':
        nested_dict[user]['completed_tasks']+=1
''''
{
'Ravi': {
'tasks': ['Data Cleaning', 'Api Integeration'],
 'total_hours': 7, 'completed_task': 2, 
 'total_task': 2
 }, 
 'Jake': {
 'tasks': ['Model Training', 'Testing & Manual Testing'],
 'total_hours': 11, 
 'completed_task': 2,
 'total_task': 0
 }, 
 'Marty': {
 'tasks': ['UI Design', 'Backend Design'],
'total_hours': 12,
'completed_task': 2,
'total_task': 2}
}
'''
#completion rate is (completed_task / total_task) * 100
# for user,value in nested_dict.items():
#     task_completed=nested_dict[user]['completed_tasks']
#     total=nested_dict[user]['total_tasks']
#     print(f'\n{user}:\n\t{value}')
#     nested_dict['completion_rate'] = (task_completed /total )* 100.0
    #.items() not allowed becuase dictionary is changing during the itertion

for user in nested_dict:
    task_completed=nested_dict[user]['completed_tasks']
    total=nested_dict[user]['total_tasks']
    # print(f'\n{user}:\n\t{value}')
    #avg_hr_per_task=total_hrs/total_tasks
    Time_taken_To_complete_All_Task=nested_dict[user]['total_hours']
    Total_Number_of_Tasks=nested_dict[user]['total_tasks']
    nested_dict[user]['avg_hours_per_task']=Time_taken_To_complete_All_Task/Total_Number_of_Tasks
    nested_dict[user]['completion_rate'] = (task_completed /total )* 100.0
    print(f'\n{user}:\n\t{nested_dict[user]}')
    del nested_dict[user]['completed_tasks']
    del nested_dict[user]['total_tasks']
''''
Upgrade Challenge (Do This Next)

Try modifying:

Only include tasks where status == "Done"

Add:

'avg_hours_per_task'
Sort users by total_hours descending
'''

for key , value in nested_dict.items():
    print(f'\n {key}:\n\t{value}')