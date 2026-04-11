alien_0={}
alien_0['color']='Red'
alien_0['points']=5
# alien_0['x']=12
# print(alien_0)
alien_01={'x_position':0,'y':25,'speed':'slow'}
alien_0=alien_0|alien_01
print(alien_0)
print(alien_01)

if alien_0['speed']=='slow':
    alien_0['x_position']=alien_0['x_position']+1
elif alien_0['speed']=='medium':
    alien_0['x_position']=alien_0['x_position']+2
elif alien_0['speed']=='fast':
    alien_0['x_position']+=3

print(f'alien new state {alien_0} and it\'s new x_position is {alien_0["x_position"]}')
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',}
print(favorite_languages)