'''
6-7. People: Start with the program you wrote for Exercise 6-1 (page 102) . 
Make two new dictionaries representing different people, and store all three 
dictionaries in a list called people . Loop through your list of people . As you 
loop through the list, print everything you know about each person 
'''
peoples=[
    {'first_name':'Marty','last_name':'Byerd','age':45,'city':'ozark'},
    {'first_name':'Wendy','last_name':'Byerd','age':40,'city':'ozark'},
    {'first_name':'jonah','last_name':'Byerd','age':12,'city':'ozark'}
]
'''
{ 'Marty_Byerd':{'age':45,'city':'ozark','birth_place':'cicago'}
}
'''
nested_dict={}
for people in peoples:
    first_name=people.get('first_name','NA')
    last_name=people.get('last_name','NA')
    full_name=first_name.title() +" "+last_name.title()
    #print(full_name)
    age=people.get('age','Na')
    city=people.get('city','NA')
    birth_place='cicago'
    # nested_dict[full_name][age]=age
    # nested_dict[full_name][city]=city
    # nested_dict[full_name][birth_place]=birth_place
    nested_dict[full_name]={
        'age':age,'city':city,'birth_place':birth_place
    }

# print(nested_dict)
for person,details in nested_dict.items():
    print(f'{person}:-')
    for key,value in details.items():
        print(f'\t{key}\t{value}')
import json
print(json.dumps(nested_dict, indent=4))
#let's do this engineering way
print("=====================================")
peoples=[
    {'first_name':'Marty','last_name':'Byerd','age':45,'city':'ozark'},
    {'first_name':'Wendy','last_name':'Byerd','age':40,'city':'ozark'},
    {'first_name':'jonah','last_name':'Byerd','age':12,'city':'ozark'}
]
'''
{ 'Marty_Byerd':{'age':45,cities:['citiy':'ozark','birthplace':'cicago']}
}'''
nested_dict={}
# group->aggregate->transform
#group->grouping data , organizing data into categories /cluster
#aggregate-> calculate summary for each group / doing mathematics calculation on data
#transform-> shape aggregate data into final shape as required format
#creating a data structure & must intinialize the data structure schema with 
# default value and avoid random adding of the data structure
# aggregate-> use loop to aggragte the data , like all the operartion to be carried
#out ,& data collected for group from source
#post loop-final metrices

#group by user first_name+last_name=Marty_Byerd,Wendy_Byerd,Jonah_Byerd -as key to dictionary to describe ds
#{{}} age,city,birth_place is schema of cluster and intisialize with default value age=0,city=[],
# nested_dict={
    
#     'Marty Byerd':{'age':45,'cities':[{'current_city':'ozark','birtplace':'cicago'}]},
#     'Wendy Byerd':{'age':40,'cities':[{'current_city':'ozark','birthplace':'cicago'}]},
#     'Jonah Byerd':{'age':40,'cities':[{'current_city':'ozark','birthplace':'cicago'}]}
# }
# for user in nested_dict:
#    for keey,value in nested_dict[user].items():
# print( nested_dict['Marty Byerd']['cities'][0]['current_city'])
# nested_dict[user]={'age':'','cities':[{'current_city':value,'birthyplace':}]}
for people in peoples:
    #people is dictionary 0->dict1,1->dict2,2->dict3
    first_name=people.get('first_name','NA')
    last_name=people.get('last_name','NA')
    full_name=first_name +" "+last_name
    if full_name not in nested_dict:
        nested_dict[full_name]={
            'age':0,
            'cities':[
                {
                    'current_city':"",
                    'birthcity':""
                }
            ]

        }
    nested_dict[full_name]['age']=people.get('age','NA')
    nested_dict[full_name]['cities'][0]['current_city']=people.get('city','NA')
    nested_dict[full_name]['cities'][0]['birthcity']='cicago'
print(nested_dict)
''''
6-8. Pets: Make several dictionaries, where the name of each dictionary is the 
name of a pet . In each dictionary, include the kind of animal and the owner’s 
name . Store these dictionaries in a list called pets . Next, loop through your list 
and as you do print everything you know about each pet 
'''
pets=[{'sheru':{'kind of animal':'dog','owner':'Ravi'}},
      {'Nova':{'kind of animal':'dog','owner':'Raj'}}
      ]
for pet in pets:
    for petname , value in pet.items():
        print(f'{petname}')
        for kindofanimal, value in value.items():
            print(f'{kindofanimal}:-\t{value}')
print('maja nhi aa raha hai')
print("\n")

pets=[{'sheru':{'kind of animal':'dog','owner':'Ravi'}},
      {'Nova':{'kind of animal':'dog','owner':'Raj'}}
      ]
'''
{Ravi:{
'petname':'sheru',
'kind of animal' 'dog'
}
Raj:{
'petname':'sheru',
'kind of animal':'dog'
}
}
'''
''''
pets=[{'sheru':{'kind of animal':'dog','owner':'Ravi'}},
      {'Nova':{'kind of animal':'dog','owner':'Raj'}}
      ]
'''
print(pets[0]['sheru'].get('owner','NA'))
petowner={}
for pet in pets:
    #creating a data structure
    # pet[] get Ravi value it's in dictionary of dictionary  pet['sheru']['owner'] sheru-key and owner 
    #is value of key sheru and it store inside the dictionary pet[key]['owner']
    #print(type(pet))
    for petname in pet:
        user=pet[petname].get('owner','NA')
        print(user)
        if user not in petowner:
            petowner[user]={
                'petname':'',
                'kind of animal':''
            }
        petowner[user]['petname']=petname #sheru
        petowner[user]['kind of animal']=pet[petname].get('kind of animal','NA')
import json
print('\n')
print(json.dumps(petowner,indent=4))
