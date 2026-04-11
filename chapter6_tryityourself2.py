'''
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output.
'''
glossary={
    'for':'looping',
    'if':'conditional statements',
    'list':'[]',
    'in':'keywords',
    'del':'very dangerous it remove everything'
}
for key, value in glossary.items():
    print(f'{key}:{value}')
# adding 5 elements more
# glossary['variable']='dynamic data storage'
print(glossary)
# glossary['dictionary.items()']='key,value'
# glossary['dictionary.keys()']='key'
# glossary['dictionary.values()']='values'
# glossary['sorted(dictionary.keys())']='key_sorted_way'
# glossary['set(dictionary.values())']='only unique value'
print(f' {glossary}\n{len(glossary)}')
# another way we can add value to dictionary
# using lists , 1 lis store keys and another value
keylist=['variable','dictionary.items()','dictionary.keys()','dictionary.values()',
         'sorted(dictionary.keys())','set(dictionary.values())']
valuelist=['dynamic data storage','key,value','key','values','key_sorted_way','only unique value']
for topic , meaning in zip(keylist,valuelist):
    glossary[topic]=meaning
print('glossary')
print(f"{glossary}\n{len(glossary)}")
# and instead of using loop we can do it in single line
print("=================================")
newglossary=dict(zip(keylist,valuelist)) # glossary have 6 new value i want previous 5
# + 6 new value together to do so in upper create a newglossary then concatenate
# dictionary to glosssay
glossary=glossary | newglossary
print(f'{glossary} \n {len(glossary)}')
print(f'Topic \tMeaning')
for key , value in glossary.items():
    print(f'{key}:\t{value}')
''''
6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
•	 Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
•	 Use a loop to print the name of each river included in the dictionary.
•	 Use a loop to print the name of each country included in the dictionary.
'''
rivers=['Ganga','Nile','Amazon','Yamuna','Brahmputra']
origincountrys=['India','Egypt','USA','India','India']
riversmapping={}
print(f'River \t Country')
for river , origincountry in zip(rivers , origincountrys):
    riversmapping[river]=origincountry
for river, country in riversmapping.items():
    print(f'{river}\t\t{country}')
print('==================Rivers===============')
for river in riversmapping.keys():
    print(f'{river}')
print('===================Country=============')
for country in riversmapping.values():
    print(f'{country}')

print('=================Sorted Rivers ===================')
for river in sorted(riversmapping.keys()):
    print(f'{river}')
'''
6-6. Polling: Use the code in favorite_languages.py (page 104).
•	 Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
•	 Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.
'''
print('==============Favorite Langauge assignment============')
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'
}
peoples=['jen','sarah','edward','erin','phil','jack']
print('===============one way to do=================')
for people in peoples:
    if people in favorite_languages.keys():
        print(f'{people} thanks for taking the poll!!')
    else:
        print(f'{people} Please take our poll')
print('======================Another way to do===============')
