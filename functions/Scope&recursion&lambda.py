# function Scope
x = 1 # Global scope 

def one():
    global x
    x= 3
    print(f'var from func. scope {x}')

print(f'var from global scope {x}')

one()
print(f'var from global scope {x}')
print('#'*60)

# function Recursion 
x = 'wwwoooorrrldd'


def cleanWord(x):

    if len(x)==1 :

        return x
    
    if x[0] == x[1]:

        return cleanWord(x[1:])
   
    return x[0]+ cleanWord(x[1:])

print(cleanWord(x))

# function Lambda >> anonymous >>>has no name
# in line without def it
# can use it in return data from another func.
# lambda used for simple func. & def handle the large task
# is one single expression not block code
# type func.
print('#'*60)

def say_hello(name) : return f'Hello {name}'

hello = lambda name , age : f'Hello {name} your age is: {age}'   

print(say_hello('ahmed'))
print(hello('mostafa',25))

# name of function :

print(say_hello.__name__)
print(hello.__name__)

print(type(hello))