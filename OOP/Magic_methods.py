# __init__ called automatically when instantiating class
# self.__class__ >> the class to which  a class instance belongs
# __str__ >> give a human readable output of object
# __len__ >> return length of container & called when use built-in len() func. on object.
# ---------------------------------------------------------------------

class skill:

    def __init__(self):

        self.skills = ['html', 'css', 'python']

    def __str__(self) -> str:

        return f'this is my skilles => {self.skills}'
    
    def __len__(self):
        return len(self.skills)
        
profile = skill()

# print(profile.__class__) # belongs to skill class

print(profile)        
print(len(profile)) 


profile.skills.append('php')
profile.skills.append('mysql')

print(profile)        
print(len(profile))

print('#' * 60)
# @Properties Decorator ---
class Member:

    def __init__(self, name, age):

        self.name = name 

        self.age = age

    def say_hello(self):

        return f'Hello {self.name}'

    @property
    def age_in_days(self):
        return self.age * 365
    
man = Member('Ahmed', 25)


# print(man.age_in_days()) # typeError
print(man.age_in_days) # property
print('#' * 60)

# ******************************************************
# Abstract Base Class =>> ABCs
# ----------------------------
# Class called abstract class if it has one or more abstract methods
# abc module in python provides infrastructure for defining custom ABCs
# by adding @absttractmethod Decoratoron method 
# ABCMeta class is a metaclass used for defining ABC
# --------------------------------------------------------------------

from abc import ABCMeta, abstractmethod


# class abstract doing nothing
class programming(metaclass=ABCMeta):

    @abstractmethod
    def has_oop(self):

        pass
    
    def has_name(self):
        pass


class python(programming):
    def has_oop(self):

        return f'Yes'

class pascal(programming):
    def has_oop(self):

        return f'No'
    

one = python()

print(one.has_oop())
print(one.has_name())
