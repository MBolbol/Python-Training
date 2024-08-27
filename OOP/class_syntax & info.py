# [01] Class is the blueprint or constructor of object.
# [02] Class instantiate >> means create instance of class.
# [03] Instance => object created from class and have their methods & attributes.
# [04] Class defined  with keyword class.
# [05] Class name eritten with pascalcase [uppercamelcase] style
# [06] Class may contains methods and attributes.
# [07] when creating object python look for built in __init__ method
# [08] __init__ method called every time you create object from class
# [09] __init__ method is initialize the data for the object 
# [10] Any method with 2 underscore in the start & end called (Dunder or magic method)
# [11] self refer to the current instance created from the class and must be first param
# [12] self can named anything. 
# [13] in py you don't need to call new() keyword to creat object.
# ------------------------------------------------------------------

# Syntax -----
# class name:
#    constructor => do instantiation [creat instance from from class]
#    each instance is separate object 
#    def __init__(self, other_data) 
#        body of function


# ---------------------------------------------------------------
class Member:
    
    def __init__(self):

        print('A new member has been added')
       

Member()


member_one = Member()
print(member_one.__class__)


# polymorphism

class A:
    def do_something(self):
        print('from class A')

        raise NotImplementedError('derived class must implement this method')
    
    
class B(A):
    pass


class C(A):
    def do_something(self):
        print('from class C')

x = C()
x.do_something()
