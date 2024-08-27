# type()
# all data in py is objects

# print(type(10))#integer
# print(type(100.256))# floating point num
# print(type("hello")) #str => string

# print(type([1,2,3,4,5])) #list > square pract []
# print(type((1,2,3,4,5))) #tuple > practes ()
# print(type({"first" : 1 ,"sec" :2 })) #dictionary >> dict {"key":value}
# print(type(2==2)) #bool >>> boolean (true or false)

# ----------------------------------------------------
# iterable VS iterator --
# ---------------------------------------------------
#[1] Iterable >> is an object contains data that can be iterated upon
#[2] ex >> (str, list, set, tuple, dict)
# -----------------------------------------------
#[1] Iterator >> is an object, used to iterate over iterable using next() mehtod return one element at a time.
#[2] can generate Iterator from iterable when using iter() method 
#[3] for loop already calls iter() method on iterable behind the scence 
#[4] gives "stopiteration" if there is no next element.
# ----------------------------------------------------------------------
name = 'Mostafa'
myiterator = iter(name)
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
# print(next(myiterator))>>>>>> stopiteration
print('#' *60)
# --------------------------------------------------------------------
# Generator func.
# is func. with 'yield' keyword instead of return.
# support iteration & return generator iterator by calling "yield"
# generator func. can have one or more yield .
# by using next() it resume from where it called yield not from begining
# when called , its not start automatically , its only give you the control
# ----------------------------------------------------------------------

def myGenerator():
    yield 1 
    yield 2 
    yield 3 
    yield 4 

gen = myGenerator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print('#' *60)

# -------------------------------------------
# loop on many iterators with zip() func.
# zip() return a zip opject contain all objects
# zip() length is length of lowest object
# ----------------------------------------------

l1 = [1, 2, 3, 4, 5]
l2 = ['A', 'B', 'C']
t1 = ('Man', 'Woman', 'Girl', 'Boy')
d1 = {'name': 'Mostafa', 'age' : 25, 'country': 'Egypt'}

ultimateList = zip(l1, l2, t1, d1.keys(), d1.values())
# print(ultimateList)

for item in ultimateList:
    print(item) # legth lowest list == 2

