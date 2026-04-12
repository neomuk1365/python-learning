raw_logs = [
    {'user': 'Ravi', 'task': 'Data Cleaning', 'hours': 2, 'status': 'Done'},
    {'user': 'Jake', 'task': 'Model Training', 'hours': 5, 'status': 'Pending'},
    {'user': 'Ravi', 'task': 'API Integration', 'hours': 3, 'status': 'Done'},
    {'user': 'Marty', 'task': 'UI Design', 'hours': 4, 'status': 'Done'},
    {'user': 'Jake', 'task': 'Testing', 'hours': 1, 'status': 'Done'}
]

nested_data = {}

for log in raw_logs:
    user = log['user']

    # Step 1: Initialize user if not exists
    if user not in nested_data:
        nested_data[user] = {
            'tasks': [],
            'total_hours': 0,
            'completed_tasks': 0,
            'total_tasks': 0
        }

    # Step 2: Update data
    nested_data[user]['tasks'].append(log['task'])
#     nested_data[user]['total_hours'] += log['hours']
#     nested_data[user]['total_tasks'] += 1

#     if log['status'] == 'Done':
#         nested_data[user]['completed_tasks'] += 1

# # Step 3: Compute completion rate
# for user in nested_data:
#     completed = nested_data[user]['completed_tasks']
#     total = nested_data[user]['total_tasks']

#     nested_data[user]['completion_rate'] = (completed / total) * 100

#     # Optional cleanup (production style)
#     del nested_data[user]['completed_tasks']
#     del nested_data[user]['total_tasks']

print(nested_data)