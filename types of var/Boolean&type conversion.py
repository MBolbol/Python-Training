# values 2 constant objects (true or false)
n = ''
print(n.isspace())
n = ' '
print(n.isspace())
print('=' * 50)
# bool()
print(bool(100))
print(bool('mo'))
print('=' * 50)

print(bool(''))
print(bool([]))
print(bool())
print('=' * 50)
# Operators
# and
age = 25 
country = 'Egypt'
rank = 10
print(age > 15)
print(country == 'Egypt')
print(age > 15 and country == 'Egypt' and rank >20 )
print('=' * 50)

# OR
print(age > 15 or country == 'Egypt' or rank >20 )

# NOT
print(not age > 15) #reverse logical case
print('=' * 50)

# type conversion
# str()
a = 100.5
print(type(a))
print(type(str(a)))
print('=' * 50)

# tuple() >>>()
c = 'bolbol' #str
d = [1,3 ,2 ,4] #list
print(tuple(d))
# list() >>>[]
# set() >>>{}
# dict() >> str not conversion , tuple should be nasted tuble
# also in the list , But set unhashable type not conversion 
######################################################################
print('=' * 50)

# User Input 
# input('Hello python')
fName = input('what is your first name?') 
mName = input('what is your middle name?') 
LName = input('what\'s your last name?') 
age = input('How old are you?') 

fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
LName = LName.strip().capitalize()
age = age.strip().capitalize()

print(f'Hello {fName} {mName:.1s} {LName} , {age} you are a young man ,\n Happy to see you')
print('=' * 50)




