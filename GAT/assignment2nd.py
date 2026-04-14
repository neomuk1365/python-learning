# Level 2 (The Deep Update):

# Start with: 
school = {'Class_A': {'Students': {'Ravi': 90}}}
school['Class_A']['Students']['Ravi']=95
print(f'{school.get('Class_A','{}').get('Students','{}').get('Ravi','NA')}')


# Task: Write one line of code to change Ravi's score to 95.

# Task: Write a safe .get() line to find a student named "Jake" without crashing. for this answer is 
name=school.get('Class_A','NA').get('Students','NA').get('jake'.title(),'na')
if name == 'jake':
    print(f'{name} is in our school')
else:
    print(f'jake is not in our school')