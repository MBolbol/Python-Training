# set items are enclosed in curly braces {}
# not orderd & not indexed

s1 = {'salah' , 'karim' , 3}
print(s1)
print(type(s1))

# slicing can not be done
# print(s1[0:1])erroe
# has only imutable data type (num , str , tuble ) lists and dict are not
s2 = {1 , 'osama' , True , (50 , 70) } #[3 , 5]   #unhashable type: 'list'
print(s2)

# items is unique
# sets methods
# s2.clear()

# union()
print(s1 | s2) # ==s1.uniou(s2)

# add()
s1.add(100)
print(s1)
# copy()
# remove() element

# discared()
s1.discard(10) #not error like remove
print(s1)

# pop()
print(s1.pop()) #pop random element
print(s1.pop())

# update() == union()

# Difference()  ==   (-)
a= {1 , 2, 3 ,4}
b= {1 , 2 , 6, 8}
print(a.difference(b))
print(b - a)

# difference_update()
a.difference_update(b)
print(a)

print('$' * 40)
# semetric_difference() == (^)

s3 = {5 , 6 , 7 , 1 , 'ali' , 'omar' }
s4 = {1 , 3 , 5 , 9}
print(s3)
print(s3.symmetric_difference(s4))
print(s3)

print('$' * 40)

s5 = {5 , 6 , 7 , 1 , 'ali' , 'omar' }
s6 = {1 , 3 , 5 , 9}
print(s3)
s3.symmetric_difference_update(s4)
print(s3)

print('$' * 40)

# intersection()  ==  (&)
x = {1 , 4 , 7 , 9 }
y = {1 , 2 , 4 ,6 , 7}

print(x.intersection(y))  #x & y
print(x)
print(y)
x.intersection_update(y)
print(x)
print(y)
print('#' * 40)

# issuperset() 

i = {1 , 4 , 7  }
j = {1 , 2 , 4 ,6 , 7}
print(i.issuperset(j))
print(j.issuperset(i))

# issupset()
print(i.issubset(j))
print(j.issubset(i))
print('#' * 40)

# isdisjoint()
f = {1 , 4 , 7 }
h = {1 , 2 , 4 ,6 , 7}
g = {11 ,20}
print(f.isdisjoint(h))
print(f.isdisjoint(g))

 
 
  


