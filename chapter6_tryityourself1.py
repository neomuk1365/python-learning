''''
6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.
'''
person={
    'first_name':'Marty',
    'last_name':'Byerd',
    'age':45,
    'city':'ozark',
    
}
# print(person.get('first_name'))
print(f'Perosn name \t{person.get('first_name')} {person.get('last_name')}')
print(f'age \t {person.get('age')}\ncity \t {person.get('city')}\nphone \t {person.get('phone','not specified')}')
'''
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.
'''
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
''''
-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
•	 Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
•	 Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.
'''
glossary={
    'for':'looping',
    'if':'conditional statements',
    'list':'[]',
    'in':'keywords',
    'del':'very dangerous it remove everything'
}
print(f'for \t {glossary.get('for')}')
print(f'if \t {glossary.get('if')}')
print(f'list \t {glossary.get('list')}')
print(f'in \t {glossary.get('in')}')
print(f'del \t {glossary.get('del')}')