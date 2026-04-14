# Transitioning from simple dictionaries to a Group -> Aggregate -> Transform
# this means taking "flat" data (like a list of records) and restructuring it into that deep, nested
cart=[['Apple', 'Fruit'], ['Carrot', 'Veggie'], ['Banana', 'Fruit']]
#{'Fruit': ['Apple', 'Banana'], 'Veggie': ['Carrot']}
# [fruitname,fruit],[vegiename,veggie],[fruitname,fruit]
sortedcart={}
for item in cart:
    thingsvalue=item[0]
    typeofthings=item[1]
    if typeofthings not in sortedcart:
        sortedcart[typeofthings]=[]
    sortedcart[typeofthings].append(thingsvalue)
print(sortedcart)
