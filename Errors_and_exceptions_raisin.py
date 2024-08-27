# Exceptions is a runtime error reporting machanism
# Exception gives you message to understand the problem
# Traceback gives you thr line to look for the code in this line
# Exceptions have types (syntaxerror, Indexerror, keyerror, ETc......)
# raise keyword used to raise your own exceptions 
# Exceptions list https://docs.python.org/3/library/exceptions.html
# ---------------------------------------------------------

# x = -10

# if x < 0:
    
#     raise Exception (f'{x} is less than zero')

# else:
#     print(f'{x} is good enouph')

# print('msg after if')

# y= 'mostafa'

# if type(y) != int:
    
#     raise ValueError('Only nums allowed')
# -----------------------------------------
# Exceptions handling by: Try >> except >> else >> finally
# Try => test code for errors
# except => handel errors
# -------------------------
# else => if no errors
# finally => run the code
# -------------------------------------

# try:
#     age = int(input('Write your age: '))

# except:
#     print('Bad, this is not integer')

# else:
#     print('Good, this is integer')

# finally:
#     print('print whatever happens')

# print(age)
# -------------------------------------------
# advanced ex.

the_file = None
the_tries = 5

while the_tries > 0:

    try: # try to open the file.

        print('Enter the file name with absolute path to open')
        
        print(f'{the_tries} tries left')

        print('example: E:/python trainning/file name.py')
        print('#'*60)

        file_name_and_path = input('file name => : ').strip()

        the_file = open(file_name_and_path, 'r' )

        print(the_file.read())

        break
    
    except FileNotFoundError:
       
        print('file not found please be sure the name is correct')
        print('#'*60)

        the_tries -= 1

    except:
        print('Error happen')
    
    finally:
        if the_file is not None:

            the_file.close()
            print('the file closed.')


else:
    print('All tries is done.')
# ------------------------------------
# Debugging code
# ----------------------------------

# type hinting---
# ---------------
# def say_hello(name) -> str: # type only
#     return f'Hello {name}'

# print(say_hello('mostafa'))