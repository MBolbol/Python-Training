# tuple items are enclosed in parentheses
# you can remove the parentheses if you want 

t1 = ('mostafa' , 'loai')
t2 = 'ahmed' , 'abdo'
print(t1)
print(t2)
print(type(t2))

# tuples are imutable >> you can not add or delete
# tuple assign values
t3 = 1 ,2 , 3 ,4 ,5 ,6
# t3[2] = 'three' >> #error 'tuple' object does not support item assignment
# tuple items are not unique
# can have different data types
# operators used in str & lists avilable in tuples

# tuple with one element   >>> put , after element

t4 = 'Bolbol', # == ('Bolbol',)
t5 = 'Ramadan'
print(t4)
print(t5)
print(type(t4))
print(type(t5))

# tuple concatenation
t6 = 8 , 9
t7 = t6 + t3
print(t7) 
print(sorted(t7))

# tuple , list , str Repeat (*)
print(t6 * 3) 

print(t6.count(8))

# Tuple Destruct

a= 'a','b','c'
x , y , z = a
print(x.capitalize())
print(y.capitalize())
print(z.capitalize())

a= 'a', 10 , 'b','c'
x , _ ,  y , z = a
print(x.upper())
print(y)
print(z)
