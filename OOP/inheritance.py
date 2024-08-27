class food: # base class (parent)

    def __init__(self, name, price):

        self.name = name
        self.price = price

        print(f'{self.name} is created from base class & its price is => {self.price}')

    def eat(self):

        print('eat method from base class')

class apple(food): # derived class (son) and it override at parent

    def __init__(self, name, price, amount):

        # food.__init__(self, name) # creat instance from base class ==

        super().__init__(name, price)

        self.amount = amount
        
        print(f'{self.name} is created from derived class & amount is => {self.amount}')

    def get_from_tree(self):

        print('get from tree from the son')
    
    def eat(self): # method overide

        print('eat method from son class')

# food_one = food('Pizza')
food_two = apple('Pizza', 30, '2 kgm')
food_two.get_from_tree()
food_two.eat()

print('#' *60)
# mltiple inhertance

class base_one:
    
    def __init__(self):
        print('base one')

    def func_one(self):
        print('func. one')

class base_two:

    def __init__(self):
        print('base two')

    def func_two(self):
        print('func. two')

class derived(base_one, base_two):
    pass


son = derived()

son.func_one()
son.func_two()

# print(derived.mro()) # Return a type's method resolution order.

class base:

    def __init__(self):
        print('base')


class derived_one(base):
    pass


class derived_two(derived_one):
    pass

s = derived_two()

