# Transitioning from simple dictionaries to a Group -> Aggregate -> Transform
# this means taking "flat" data (like a list of records) and restructuring it into that deep, nested
cart=[['Apple', 'Fruit'], ['Carrot', 'Veggie'], ['Banana', 'Fruit']]
#{'Fruit': ['Apple', 'Banana'], 'Veggie': ['Carrot']}
# [fruitname,fruit],[vegiename,veggie],[fruitname,fruit]
#declare the dictionary
sortedcart={}
for item in cart:
    typesofthings=item[1]
    if typesofthings not in sortedcart:
        sortedcart[typesofthings]=[]
    #filling the things
    sortedcart[typesofthings].append(item[0])
print(sortedcart)