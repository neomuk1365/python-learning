#Dictionary
'''
Consider a game featuring aliens that can have different colors and point
values. This simple dictionary stores information about a particular alien:
'''
alien_0={'color':'Red','points':5}
print(alien_0['color'])
print(alien_0['points'])
'''
A dictionary in Python is a collection of key-value pairs. Each key is connected
to a value, and you can use a key to access the value associated with that key.
A key’s value can be a number, a string, a list, or even another dictionary.
In fact, you can use any object that you can create in Python as a value in a
dictionary.
'''
'''
A dictionary key must be hashable. 
n Python, "hashable" usually means the object must be immutable (it can't change).

Strings and Numbers are immutable, so they work perfectly as keys.

Lists and Dictionaries are mutable (they can change), so they cannot be used as keys directly.
If you try to use a list as a key, Python will throw a TypeError: unhashable type: 'list'. 
To get around this, we use Tuples (for lists) or Frozensets (for dictionaries).
'''
new_points=alien_0['points']
print(f'you have just earned {new_points} points!')

#adding new key-value pairs
#seeing the state of the alien
print(alien_0)
#alien position starts from upper left so  x=0 & y=25mm
alien_0['x_cordinate']=0
alien_0['y_cordinate']=25
print(alien_0)
#Python doesn’t care about the order in
#which you store each key-value pair; it cares only about the connection
#between each key and its value.
#starting with the empty dictionary
alien_0={}
# print(alien_0)
alien_0['color']='Green'
# print(alien_0)
alien_0['points']=5
# print(alien_0)
'''
you’ll use empty dictionaries when storing user-supplied data
in a dictionary or when you write code that generates a large number of
key-value pairs automatically
'''
#Modifying the values in dictionary
print(alien_0)
alien_0['color']='Red'
alien_0['points']=10
print(alien_0)
'''
let’s track the position of an alien that
can move at different speeds. We’ll store a value representing the alien’s
current speed and then use it to determine how far to the right the alien
should move:
'''
# alien_0={'x_position':0,'y_position':25,'speed':'medium'}
# print(alien_0)
#i want a dictionary way like it must have before attached 2 key-value pairs
#one-way 
# alien_0['x_position']=0
# alien_0['y_position']=25
# alien_0['speed']='medium'
print(alien_0)
#let's google another way it's looks like labour task
alien_01={}
alien_01['x_position']=0
alien_01['y_position']=25
alien_01['speed']='medium'
#using | operator or using for loop 2 types of data there in real life csv and json
alien_0=alien_0 | alien_01
print(alien_0)
#move the alien to right
#how far any object move it's depend on speed speed=['slow','medium','fast']
#if speed slow x chaneges =1 , medium x changes=2, fast x changes=3
#how to acces alien_0 speed alien_0['speed']



# upadte x and y position parallely changing y_postion is tricky i don't know when to use cordinate to become
#positive y and negative y so we will se later
#copy code above and add one more line in every conditional statement

if alien_0['speed']=='slow':
    alien_0['x_position']=alien_0['x_position']+1

elif alien_0['speed']=='medium':
    alien_0['x_position']=alien_0['x_position']+2
elif alien_0['speed']=='fast':
    alien_0['x_position']+=3

print(f'alien new x position {alien_0} and it\'s changed x position {alien_0['x_position']}')
#Removing key-value pair
del alien_0['points']
print(alien_0)
print("==============================Day 2=============================")
favorite_numbers={
    'marty byrde':5,
    'wendy byrde':10,
    'ruth langmore':13,
    'darlen snell':45,
    'jonah byrde':87
}
print(f'person name \t FavoriteNumber')
print(f'{'marty byrde'.title()} \t {favorite_numbers.get('marty byrde')}')
print(f'{'wendy byrde'.title()} \t {favorite_numbers.get('wendy byrde')}')
print(f'{'ruth langmore'.title()} \t {favorite_numbers.get('ruth langmore')}')
print(f'{'darlen snell'.title()} \t {favorite_numbers.get('darlen snell')}')
print(f'{'jonah byrde'.title()} \t {favorite_numbers.get('jonah byrde')}')
print(f'let\'s do it in engineering way let\'s write less')
favorite_numbers={
    'marty byrde':5,
    'wendy byrde':10,
    'ruth langmore':13,
    'darlen snell':45,
    'jonah byrde':87
}
for key,value in favorite_numbers.items():
    print(f'\n{key.title()}: {value}')
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'
}
for name,language in favorite_languages.items():
    print(f'{name.title()}\'s favorite language is : {language.capitalize()}')
print("=================Looping Through All the Keys in a Dictionary================")
favorite_language={'jen':'python','sarah':'c','edward':'rust','phil':'python'}
print("looping through key value pairs")
for name in favorite_language.keys():
    print(name.capitalize())
friend=['marty','phil','sarah']
for name in favorite_language.keys():
    if name in friend:
        print(f'{name}\'s your favorite language is {favorite_language.get(name).title()}')
    else:
        print(f'{name}\'s favorite language :\t {favorite_language[name].title()}')
print("=======================Another way=============================")
favorite_language={'jen':'python','sarah':'c','edward':'rust','phil':'python'}
friend=['marty','phil','sarah']
for name in favorite_language.keys():
    print(f'Hi {name}.')
    if name in friend:
        print(f'{name}, i see you love {favorite_language.get(name).capitalize()}!')
if 'erin' not in favorite_language.keys():
    print(f'erin please take our pol!!')
print("======Looping Through a Dictionary’s Keys in a Particular Order====")
for name in sorted(favorite_language.keys()):
    print(f'{name.title()} thank\'s for taking our poll!!')
print(favorite_language)
print("==================Looping Through All Values in a Dictionary====================")
for language in favorite_language.values():
    print(language)
print("This approach pulls all the values from the dictionary without checking for repeats")
print("i want all unique value the we can wrap value in sets")
print("To see each language chosen without repetition, we can use a set. A set is a collection in which each item must be unique:")
for language in set(favorite_language.values()):
    print(language.title())
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
for options in Margherita_Pizza.keys():
    for value in Margherita_Pizza[options]:
        print(f'{options}\t {value}')
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
    
