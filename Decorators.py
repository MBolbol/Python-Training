# decorators called sometime meta programming
# everything in py is object even func.
# decorator take func. and add some functionality and return it
# decorator wrap other func. & enhance their behaviour 
# decorator is higher order func. (func. accept func. as parameter)
# ------------------------------------------------------------------
# name = 'mostafa'
def myDecorator(func): # Decorator

    def neastedfunc(name): #any name just for decoration 

        print('Before')

        func(name) # execute function

        print('After')

    return neastedfunc # return all data

@myDecorator

def sayHello(name):
    print(f'Hello {name.capitalize()}')

@myDecorator

def sayHowAreYou(name):
    print(f'{name.capitalize()}, how are you ?')

# afteDecoration = myDecorator(sayHello)

# afteDecoration()

sayHello('Ahmed')

sayHowAreYou('Bolbol')

print('#' *60)
# -------------------------------------------------
# speed test
from time import time
def speedTest(func):

    def wrapper():

        start = time()

        func()

        end = time()

        print(f'Function Running time is: {end - start} sec.')
    
    return wrapper

@speedTest

def bigLoop():

    for num in range(1, 15000):
        print(num)

bigLoop()
    
    