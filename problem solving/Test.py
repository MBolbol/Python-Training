# test for 11 >> 18
# "Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt
name = 'Osama'
age = "38"
country = 'Egypt'
print(f'\"Hello \'{name}\', How You Doing \\ \"\"\" Your Age Is \"{age}\"\" + And Your Country Is: {country} ')
print('=' * 50)

print(f'\"Hello \'{name}\', How You Doing \\\n \"\"\" Your Age Is \"{age}\"\" +\n And Your Country Is: {country} ')
print('=' * 50)

# 03
name = 'Mostafa'
# print('Second Letter is ' + f'{name[1:2]}')
x = name[1:2]
print('Second Letter is ' + f'\"{x}\"')
y = name[2:3]
print('Third Letter is ' + f'\"{y}\"')
z = name[-1]
print('Last Letter is ' + f'\"{z}\"')
print('=' * 50)

# 04
name = 'Elzero'
a = name[1:4]
b = name[0:5:2]
c = name[-2:-7:-2]
print(f'\"{a}\"')
print(f'\"{b}\"')
print(f'\"{c}\"')
print('=' * 50)

# 05
name = "#@#@Elzero#@#@"
print(name.strip('#@'))

# 06
num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"
print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))
print('=' * 50)

# 07
name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20,'@'))
print(name_two.rjust(20,'@'))
print('=' * 50)
# 08
name_one = "OSamA"
name_two = "osaMA"
print(name_one.capitalize())
print(name_two.swapcase())
print('=' * 50)

# 09
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count('Love'))
# 10
name = "Elzero"
print(name.index('z'))
# 11 ,12
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace('<3' , 'Love' , 1))
print(msg.replace('<3' , 'Love' , 2))
print('=' * 50)

# 13
name = "Mostafa"
age = 38
country = "Egypt"
# My Name Is Osama, And My Age Is 38, And My Country Is Egypt
print(f'My Name Is {name}, And My Age Is {age:d}, And My Country Is {country}')

# Test 2 from 19 >>> 20
print('=' * 50)
num = 10
print('{:.10f}'.format(num))
print(f'{num:.10f}')
print('=' * 50)
# 05
print(21%4)

print(97%20)
print(97/20)
print(97//20)
# Test 3 from 21 >>> 23
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])
# print(friends.pop(0))
print('=' * 50)
# 04
friends[3]=friends[4]= 'Elzero'
print(friends)
friends.insert(0 ,"Nasser")
print(friends)
friends.insert(6,"Salem")
print(friends)
print('=' * 50)
friends.remove('Osama')
friends.remove('Ahmed')

print(friends)
print('=' * 50)
# 07 , 08
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
friends.extend(employees)
friends.extend(school)
print(friends)
friends.sort()
print(friends)
friends.reverse()
print(friends)
# Test 4 from 24 >>> 25
print('=' * 50)
friends = ("Osama", "Ahmed", "Sayed")
# friends.remove("Osama") #tuple imutable
l1 = list(friends)
l1[0] = 'Elzero'
friends = tuple(l1)
print(friends)
print(f'{len(friends)} Elemets')
print('=' * 50)

#03 
nums = (1, 2, 3)
letters = ("A", "B", "C")
x = nums + letters
print('nums_and_leters_one = ' + f'{x}')
print(len(x))
print('=' * 50)
# 04
my_tuple = (1, 2, 3, 4)
a ,b , _ ,c = my_tuple
print(a)
print(b)
print(c)
print('=' * 50)

# test 5  from 26>>32
# 01
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = set(my_list)
unique_list = list(unique_list)
print(unique_list)
unique_list.pop()

print(unique_list)






