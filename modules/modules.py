# built in modules
# it is a file contain a set of func.
# you can import module in your app to help you
# you can import multiple modules 
# you can creat your own modules
# it saves your time
#----------------------------------------------
# import main module
# import random == from random import *

# print(random)
# print(f'Random float numbers {random.random()}')

# shaw all func. inside module
# print(dir(random))

# import one or two func.
# from random import randint, randrange
# print(f'Random integer {randint(50, 200)}')
# print(f'Random rang {randrange(50, 200)}')

# creat your module
# import sys

# sys.path.append(r"E:\python trainning\files\bolbol.py")
# print(sys.path)

# import bolbol
# print(dir(bolbol))
print('#'*60)

# bolbol.sayHello('mostafa')
# bolbol.sayHowAreYou('mostafa')
# bolbol.sayHowOld('mostafa')

from bolbol import sayHowOld
sayHowOld('mostafa')

from bolbol import sayHowAreYou as syy
syy('mostafa')

import bolbol as b

b.sayHello('ahmed')
b.sayHowAreYou('abdo')
b.sayHowOld('ali')

# ---------------------------------------------
# install external packages
# with python package manager >>> pip
# https://pypi.org/

import pyfiglet
import termcolor
print(termcolor.colored(pyfiglet.figlet_format('Mostafa_Bolbol'), color= 'red' ))

