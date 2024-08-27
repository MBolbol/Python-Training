# dict items are in curly Braces
# dict items contain {key : value}
# keys need to be imutable => num , str , tuple ,,,(lists not allowed)
# values can have any data type 
# key must be uniqe
# dict not ordered , you access its element with key.

user = {
    'name' : 'Mostafa' , 
    'age' : 25 ,
    'nationality' : 'Egyption' ,
    'skills' : ['python' , 'HTML' , 'CSS'] ,
    'rating' : 84.3

 } 
print(user)
print(type(user))

print(user['skills'])
print(user['age'])
print(type(user['skills']))
print(user.keys())
print(user.values())

# two-dimentional dict
lang = {
    'one' : {
        'name' : 'HTML' , 
        'progress' : '70%'
    } ,
    'two' : {
        'name' : 'py' , 
        'progress' : '90%'
    }
}
print(lang)
print(type(lang))
print(lang['one']['name'])
print(len(lang))

# methods 
# clear()
# update({key : value})
user['city'] = 'zagazig'
print( user)
user.update({'club':'Ahly'})
print( user)
# copy() >> shallow copy

# setdefault
print(user.setdefault('tall' , 173))
print(user.setdefault('name' , 173))

print(user)

print('='*50)

# popitem() last item
print(user.popitem())
print(type(user.popitem()))
# items 
allitems = user.items()
print(allitems)
print(type(allitems))

# fromkeys
a = ('one' , 'two', 'three')
b = 1
c = 2
d = 3
print(dict.fromkeys(a ,(b , c , d) ))





