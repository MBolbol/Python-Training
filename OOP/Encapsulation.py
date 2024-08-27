# Restrict access to data stored in attributes and methods 

# public :
# - every attribute and method that we used so far is public 
# - Attributes & methods can be modified and run from everywhere 
# - inside our outside class 

# Protected :
# - Attributes & methods can be accessed from within class and subclass 
# - Attributes & methods prefixed with one underscore (_)

# private :
# - Attributes & methods can be accessed from within class or object only
# - Attributes can't modified from outside class
# - Attributes & methods prefixed with two underscore (__)
# ---------------------------------------------------------------------
# Attributes = variables = properties
# ----------------------------------------

# class Member:

#     def __init__(self, name):

#         self.name = name # public


# one = Member('Mostafa')
# print(one.name)

# one.name = 'Bolbol'
# print(one.name)
# ------------------------
# protected:

# class Member:

#     def __init__(self, name):

#         self._name = name # protected


# one = Member('Mostafa')
# print(one._name)

# one._name = 'Bolbol'
# print(one._name)

# private
class Member:

    def __init__(self, name):

        self.__name = name # private

    def say_hello(self):
        return f'Hello {self.__name}'
    
# Getters & Setters ---
  
    def get_name(self):

        return self.__name
    
    def set_name(self, new_name):

        self.__name = new_name

one = Member('Mostafa')

print(one.say_hello())
print(one.get_name())

one.set_name('Bolbol')
print(one.get_name())


# print(one._Member__name)
# print(one.__name)

# one._name = 'Bolbol'
# print(one._name)



