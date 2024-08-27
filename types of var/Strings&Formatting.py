# "in double quote" & 'single'
text= 'this is single quote "test"'
print(text)
# '''''' or """"""(triple quote) to multi line & escape char 
x = '''first
second
third'''
print(x)
# indexing & slicing
# All data in python is object
# object contain elements
# Every element has its own index use ZERO Based indexing
# Use square Brackets to access element parts of string , tuple or lists

# Indexing (access single item)
print(text[-1])
print(text[0])
print(text[10])

# Slicing (access multiple sequence items) [start:end:step]
# end not included
print(text[2:5])
print(text[7:10])
print(text[5:20:2])

# strings methods
print(len(text)) 
# strip() rstrip() lstrip()
# a= '    I love python      '
# print(a.strip())
# print(a.rstrip())
# print(a.lstrip())
b= '#####I love python#######'
print(b.strip("#"))
print(b.rstrip("#"))
print(b.lstrip("#"))
# title()
print(text.title())
a= 'I love 3d and 5g'
print(a.title())
# capitalize
print(a.capitalize())
# zfill >>>zero fill on left
c,d,e ='1' , '11' , '111'
print(c.zfill(3))
print(d.zfill(3))
print(e.zfill(3))
# split(seprator,MAX split) & rsplit >> from right
print(a.split())
# center()
name = "Mostafa"
print(name.center(9,'#'))
print(name.center(15,'*'))
# count()
print(a.count('d'))
# swapcase()
print(name.swapcase())
# satrtswith() & endswith() >>> Boolean
print(name.startswith('M'))
print(name.startswith('s'))
# index(substr , start , end) 
print(a.index('d')) #if substr not found >> error
print(a.find('k'))  #if substr not found >> -1

# rjust() & ljust()
print(name.rjust(10,'*'))
print(name.ljust(15,'*'))

# splitlines
print(x.splitlines())
# expandtabs()
# ************
# istitle() >>> boolean
# isidentifier()> ""
# ****************************************
# replace(old , new , count)
print(x.replace("first",'one'))
print(x.replace("first",'one',3))

# join(iterable)
myList = ['Mostafa','Bolbol', 'Ramadan']
print('-'.join(myList))
print('@'.join(myList))

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# strings Formatting
age =36
rank = 10
print('My name is: '+ name)
# use placeholder %s >> string , %d >> int = digital ,
#  %f >>float %.1f num of 0000 after .....
print('My name is: %s And my age is: %d' %(name, age))
print('My name is: %s, And my age is: %d, And my rank is: %.2f' %(name, age , rank))
n = 'Bolbol'
l = 'python'
y = 10
print('I am %s, I learned %s, for about %d years' %(n , l , y))
print('I am %s, I am %s Developer with %d years experience' %(n , l , y))
#  truncate string

t= 'hello people of elzero web school i love you all'
print('Message is %.5s' %t)

# new ways  {} = {:s}  .format >>>{:f},{:d}
print('Message is {}' .format(t))
print('My name is: {}, And my age is: {}, And my rank is: {}' .format(name, age , rank))
print('My name is: {:s}, And my age is: {:d}, And my rank is: {:.3f}' .format(name, age , rank))

print('Message is {:.13}' .format(t))

money = 100254365945
print('my money in the bank is: {:,d}' .format(money))

# rearrange items
a , b, c = 'one', 'two', 'three'
print('Hello {} {} {}' .format(a ,b ,c))
print('Hello {2} {1} {0}' .format(a ,b ,c))

# new f'asasasa{}, sdsd{}'
print(f'My name is: {name}, And my age is: {age}, And my rank is: {rank}' )

print(f'My name is: {name}, And my age is: {age:d}, And my rank is: {rank:.2f}' )

