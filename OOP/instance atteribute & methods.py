# Self : point to instance create from class.
# instance atteributes: it is defined inside the constructor.
# ----------------------------------------------------------------
# instance methods: take self parameter which point to point to instance create from class.
# instance methods cane have more than one parameter like any funcrion. 
# instance methods can freely access attributes and methods on the object.
# instance methods can access the class itself.
# ---------------------------------------------------------------

# class attributes ---
# Attributes defiend outside constractor.
# ---------------------------------------------------
# Class methods:
# - marked with @classmethod decorator to flag it is as class method
# - it take cls parameter not self to point to class not instances
# - it doesn't require creation of class instance
# - used when you want to do something with class itself
# -----------------------------------------------------
# static methods:
# - it take no parameters
# - its bound to class not instance
# - used when doing something doesn't have access to object or class but related to class
# ---------------------------------------------------------------------

class Member:

    not_allowed_names = ['Hell', 'Shit']

    users_count = 0

    @classmethod
    def show_users_count(cls):

        print(f'we have {cls.users_count} users in our system')

    @staticmethod
    def say_hello():

        print('hello from static method')


    def __init__(self, first_name, middle_name, last_name, gender): #constractor func
        
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name

        self.gender = gender

        Member.users_count += 1
    # methods
    def full_name(self):

        if self.fname in Member.not_allowed_names:
            raise ValueError('this name not allowed')
        
        else:
            return f'{self.fname} {self.mname} {self.lname}'

    def name_title(self):

        if self.gender == 'male':
            return f'Hello Mr.{self.fname}'
        
        elif self.gender == 'female':
            return f'Hello Miss.{self.fname}'
        
        else:
            return f'Hello {self.fname}'
    
    def all_info(self):

        return f'{self.name_title()}, your full name is: {self.full_name()}'

    def delete_user(self):

       Member.users_count -= 1

       return f'user {self.fname} is deleted.'

member_one = Member('Shit' , 'ali', 'abas', 'male')

member_two = Member('Abdo', 'mostafa', 'akmal', 'male')

member_three = Member('Mona', 'ramadan', 'shaban', 'female')

# print(dir(Member))

# print(member_one.fname, member_one.mname, member_one.lname)
# print(member_two.fname, member_two.mname, member_two.lname)
# print(member_three.fname, member_three.mname, member_three.lname)

# print(member_one.full_name())

# print(member_two.all_info())
# print(member_three.all_info())

# print(member_one.delete_user())

# print(Member.users_count)

Member.show_users_count()

Member.say_hello()