print('======================DAY 3=================')
user_1={'name':'Ravi Ranjan','phone':'09087654321','email':'xyz@gmail.com'}
user_2={'name':'jake','phone':'1234567890','email':'jake@gmail.com'}
user_3={'name':'marty','phone':'2134567890','email':'marty@gmail.com'}
users=[user_1,user_2,user_3]
print(users)
print("=========================")
#looping of dictionary lsit
count=1
for user in users:
    print(f'User_{count} details:-')
    # for key, value in user.items():
    #     print(f'{key} {value}')
    print(user)
    count+=1
print("=======================")
#in real life different users i want to create a list of 30 different user fleet
# info but not manually till now i haven't read like this in this example showing 30 items 
# of 1 user
# empty list
Listsofusers=[]
#make 30 items of 1 user
for index in range(30):
    new_user={'name':'marty','phone':'0987654321','email':'marty@gmail.com'}
    #adding in last elements from right side of list=Listsofusers
    Listsofusers.append(new_user)
#printing 5 user data
for user in Listsofusers[:5]:
    print(user)
print('...')

#printing how many user data we have right now
print("The users we have right now is"+" "+str(len(Listsofusers)))
print("=======================")
aliens=[]
for i in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
#change the first 3 alien character
for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color']='Yellow'
        alien['points']=10
        alien['speed']='medium'
#show first 5 alien
for alien in aliens[:5]:
    print(alien)
print('...')
print('=======================A list in a dictionary==================')
Margherita_Pizza={
    'Change Size':['Regular (Serves 1)','Medium (Serves 2)','Large (Serves 4)'],
    'Change Crust':['New Hand Tossed','100% Wheat Thin Crust','Cheese Burst','Fresh Pan Pizza'],
    'Add Veg Toppings':['Paneer','Fresh Tomato','Onion','Crisp Capsicum','Red Pepper'],
    'Add Non-Veg Toppings':['Peri-Peri Chicken','Chicken Tikka','Chicken Sausage','Chicken Keema']
}
#describe the Marherita_Pizza
# for options in Margherita_Pizza.items():
#     for value in Margherita_Pizza[options]:
#         print(f'{options}')
#         print(f'{value}')
'''
  File "e:\Learning python\chapter6\chapter6_learning.py", line 222, in <module>
    for value in Margherita_Pizza[options]:
                 ~~~~~~~~~~~~~~~~^^^^^^^^^
TypeError: cannot use 'tuple' as a dict key (unhashable type: 'list')
Error because .items() return a (key,value) tuple 
'''
#describe the Marherita_Pizza
# for options in Margherita_Pizza.keys():
#     for value in Margherita_Pizza[options]:
#         print(f'{options}\t {value}')
#instead of this this will be better
for options, choices in Margherita_Pizza.items():
    print(f'\n{options}:')
    for choice in choices:
        print(f'\t-{choice}')
 # i want to add the ruppes also along with all value of dictionary
print("===========================Adding the rupees for every option")
Margherita_Pizza1= {
    'Change Size':[{'Regular (Serves 1)':109,'Medium (Serves 2)':239,'Large (Serves 4)':449}],
    'Change Crust':['New Hand Tossed','100% Wheat Thin Crust','Cheese Burst','Fresh Pan Pizza'],
    'Add Veg Toppings':['Paneer','Fresh Tomato','Onion','Crisp Capsicum','Red Pepper'],
    'Add Non-Veg Toppings':['Peri-Peri Chicken','Chicken Tikka','Chicken Sausage','Chicken Keema']
}  
for options, optionsvalue in Margherita_Pizza1.items():
    #optionsvalue is list of dictionary
    #how to access list of dictionary
    for element in optionsvalue:
        #here element is different dicitonary so dictionary way
        if type(element) is dict:
            for variety, cost in element.items():
                print(f'{options}\t{variety}\t{cost}')    
    # for key,value in optionsvalue.items():
    #     print(f'{options} {key} {value}')
        else:
            print(f'{options}\t {element}')
print(f'Fixes proposed by gemni')
print(f'\n')
print(f'We want our data structure to be predictable so structure should be consistent')
Margherita_Pizza2= {
    'Change Size':[{'Regular (Serves 1)':109,'Medium (Serves 2)':239,'Large (Serves 4)':449}],
    'Change Crust':[{'New Hand Tossed':239,'100% Wheat Thin Crust':289,'Cheese Burst':339,'Fresh Pan Pizza':289}],
    'Add Veg Toppings':[{'Paneer':'+60','Fresh Tomato':'+60','Onion':'+60','Crisp Capsicum':'+60','Red Pepper':'+60'}],
    'Add Non-Veg Toppings':[{'Peri-Peri Chicken':'+75','Chicken Tikka':'+75','Chicken Sausage':'+75','Chicken Keema':'+75'}]
}
print(f'key as string & value as a dictionary')
for  category,choices in Margherita_Pizza2.items():
    print(f'\n{category}:-')
    # for choice,rupya in choices.items():
    #     print(f'\t{choice}\tRs.{rupya}') # ye nhi chalega choices list hai and uske andar dictionary hai
    for _ in range(len(choices)):
        for choice , rupya in choices[_].items():
            print(f'\t{choice}\tRs.{rupya}')
margherita_pizza = {
    "size": {
        "regular": 109,
        "medium": 239,
        "large": 449
    },
    "crust": {
        "hand_tossed": 239,
        "wheat_thin": 289,
        "cheese_burst": 339,
        "pan": 289
    },
    "veg_toppings": {
        "paneer": 60,
        "tomato": 60,
        "onion": 60,
        "capsicum": 60
    },
    "non_veg_toppings": {
        "peri_peri_chicken": 75,
        "chicken_tikka": 75
    }
}

for category, options in margherita_pizza.items():
    print(f"\n{category.upper()}:")
    for name, price in options.items():
        print(f"  {name} -> Rs.{price}")
print('A dictionary inside Dictionary')
MenuMargerita={
        'size':{
                'Regular (serve 1)':109,
                'Medium (Serve 2)':239,
                'Large (Serve 4)':449
                },
        'crust':{ 'New Hand Tossed':239,
                 '100% Wheat Thin Crust':289,
                 'Cheese Burst':339,
                 'Fresh Pan Pizza':289
                 },
        'Add Veg Toppings':{'Paneer':'60',
                            'Fresh Tomato':'60',
                            'Onion':'60',
                            'Crisp Capsicum':'60',
                            'Red Pepper':'60'
                            },
        'Add Non-Veg Toppings':{'Peri-Peri Chicken':'75',
                                'Chicken Tikka':'75',
                                'Chicken Sausage':'75',
                                'Chicken Keema':'75'
                                }
}
print(MenuMargerita)
print('Not looking good make it more structure way of looking')
print(f'Menu Margerita Pizza offering Customization')
for options,choices in MenuMargerita.items():
    #return {key,dictionary}
    #key->option and dictionary as choices
    print(f'\n{options}:-')
    for choice , rupya in choices.items():
        #return choice-string of choice 
        #rupya as it's money of chocie
        print(f'\t{choice} {rupya}')
print('let\'s run how it look')
print('it\'s really looking great')
print(f'let\'s acces the dictionary and use conditional as well')
# for options, choices in MenuMargerita.items():
