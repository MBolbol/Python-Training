# function is a reusable block of code do a task
# it run when you call it
# function accept element to deal with called [parameters]
# function can do the task without return data
# function can return data after job is finished
# it create to prevent dry (don't repeat your self)
# function accept elements when you call it called [Arguments]
# there's a built-in function & user defined functions
# -----------------------------------------------------------

# def functon_name():  #define function
#     print('hello python')

# functon_name() #call it

# def functon_name():  #define function
#     return 'hello python' #retun data & not show

# print(functon_name()) #call it

# Parameters & arguments
# def        =>  function keyword [define]
# say_hello  =>  func. name
# name       =>  parameter
# print(f'Hello {name}') => Task
# say_hello('ahmed') => ahmed => argument


print('#'*60)

def addition(n1 , n2):
    if type(n1) != int or type(n2) != int :
        print('only integers allowed')
    else:
        print(n1 + n2)

addition('20', 30)

print('#'*60)

def full_name(first, middle, last):
    print(f'Hello {first.capitalize()} {middle.capitalize():.1s} {last.capitalize()}')

full_name('mostafa' , 'bolbol', 'ramadan')
print('#'*60)

# function packing, unpacking arguments *args

# l = [1, 2, 3, 4]
# print(*l) astrisk
# a, b, c = 'ahmed', 'abdo', 'mostafa'

def say_hello(*people): 
    # people = [n1, n2, n3, n4]
    for name in people:
    
        print(f'Hello {name}')

say_hello('ahmed', 'abdo', 'mostafa', 'bolbol')

print('#'*60)
def show_details(name, *skills):
    print(f'Hello {name.capitalize()} your skills is: {skills}')

show_details('mostafa','html', 'css', 'js', '...')

# Default parameters
def say_hello(name, age, country = 'unknown'): # Default parameters must be last parameters 
    # people = [n1, n2, n3, n4]
    # for name in people:
    
        print(f'Hello {name.capitalize()} your age is {age},you are from {country}')

say_hello('bolbol', 25,)

# function packing, unpacking arguments keyward **kwargs
print('#'*60)
def show_skills( **skills): #needed dict
    print(type(skills))

    for skill , value in skills.items():

        print(f'Hello your skills is: {skill} => {value}')

show_skills(python = '80%', html = '70%', css = '40%' )
print('#'*60)

# trainings 
s1 =('css','js', 'php')

s2 = {'html' : '60%', 'python' : '80%'}

def show_details(name, *skills, **skillswprogress):
    
    print(f'Hello {name.capitalize()} skills without progress is: ')
    
    for skill in skills:
        print(f'- {skill}')
    
    print(f'skills with progress is:' )
    
    for key, value in skillswprogress.items():
        print(f'- {key} => {value}')
#*s1=>> 'css','js' # **s2 =>> html = '60%', python = '80%'
show_details('mostafa',*s1 ,**s2 )
