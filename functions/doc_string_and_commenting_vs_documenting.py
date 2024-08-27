'''
   How to use doc string 

'''
# doc_string and commenting Vs Documenting ----
# [1] Documentation string for class, module or func 
# [2] can be accessed from the help and doc attributes
# [3] made for understanding the functionality of complex code
# [4] theres one line and multiple line doc string
# --------------------------------------------------------------
import pylint

def func(name):

    '''This is function to say Hello from Bolbol''' #not comment >>> single line doc string

    print(f'Hello {name.capitalize()}')

func('mostafa')

print(func.__doc__) # printing doc string with attributes __doc__

help(func)
# --------------------------------------------------------------------
# Installing and usr pylint for better code ---
# -------------------------------------------------------------------
def say_hello(name):
    '''func. to say hello to person'''
    msg = 'Hello'
    return f'{msg} {name}'
say_hello('Mostafa')

# print(dir(pylint))
# print pylint in terminal ??/10 
print(pylint.run_pylint([r'e:/python trainning/doc_string_and_commenting_vs_documenting.py']))
