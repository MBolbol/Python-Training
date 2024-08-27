# all()
# any()
# bin()
# id()
# ---------
# all()

l = list(range(1,5))
# l.append([])
print(l)

if all(l):
    
    print('All elements is true')
else:
    print('there is at least one element is false')
# any()
print('#'*60)
l2 = [0,0,[]]
if any(l2):
    
    print('there is at least one element is true')
else:
    print('All elements is false')
print('#'*60)
# bin()
print(bin(4))
# id() place (address in memory)
print('#'*60)
a= 1
b= 2
print(id(a))
print(id(b))
print('#'*60)
# -------------------------------
# sum() , round(), range(), print()
# sum(iterable , start)
print(sum(l))
print(sum(l , 20))

print('#'*60)
# round(float , num of digit(after .) )
print(round(100.3265548, 2))
print(round(100.78965, 1))
print(round(100.78965))
print('#'*60)
# range(start , end , step) >>>not incloding the end (before the end)
x= tuple(range(1,10))
y= set(range(1,10,3))
print(x)
print(y)
print('#'*60)

# print() default separator is space sep=' '
print('Hello MOSTAFA')
print('Hello','MOSTAFA') #in the same line
print('Hello','MOSTAFA', sep='|') 
print('Hello','MOSTAFA','BOLBOL','RAMADAN', sep='@') 
print('#'*60)
#  end='\n' default in print
print('How Are', end=' ')
print('you, hope good', end=' & ')
print('how old are you', end='?')
print('#'*60)

# ********************************************
# abs() , pow(), min() , max() , slice()
# ----------------------------------
# abs()
x= -1
print(abs(x))
print(abs(-50))
print('#'*60)

# pow(base, exp, mod) ###modulus
print(pow(2,2))
print(pow(4,3,2)) # (4**3) % 2
print(pow(5,4))
print(pow(5,4,3)) # (5**4) % 3
print('#'*60)

# -----------------
# min(item, item,...,or iterator)
print(min(3,7,1,5,12))
x = range(0 , 10)
print(min(x))
y = ['s', 'z','l', 'd']
print(min(y))

print('#'*60)

# -----------------
# max()
print(max(3,7,1,5,12))
x = range(0 , 10)
print(max(x))
y = ['s', 'z','l', 'd']
print(max(y))

print('#'*60)
# ----------------------
# slice(start , stop , step)
a = 'mostafa'

print(a[slice(1, 7, 2)])
print('#'*60)
# -----------------------------------
# [1] map called map because it map the function on every element
# [2] function can be pre-defined func. or lambda func. 
# [3] map(function , itrator)
# ----------------------------
# pre-defined func.

# def formatText(name):

#     return f'- {name.strip().capitalize()} -'

# lNames = ['MOstafa', 'abDO', 'aHMed', 'OmAr']

# formatedNmae = map(formatText, lNames )
# # print(formatedNmae)
# for n in formatedNmae:
#     print(n)

print('#'*60)
# --------------------------------------
# lambda func.
    
# def formatText(name):

#     return f'- {name.strip().capitalize()} -'
    

lNames = ['MOstafa', 'abDO', 'aHMed', 'OmAr']

formatedNmae = map((lambda name : f'- {name.strip().capitalize()} -')  , lNames )
# print(formatedNmae)
for n in formatedNmae:
    print(n)
# --------------------------------------------------
# [1]Filter(func. , iterator)
# [2]it run a func. on every element
# [3]func. pre-defined or lambda func.
# [4]filter out all elements for which the func. return True only
# [5]func. need to return boolean value
# -------------------------------------------------
print('#'*60)
# ex 1
def checkNumbers(num):

        return num > 10

myNum = [1, 12, 5, 60, 23]

result = filter(checkNumbers , myNum)

for n in result:
    print(n)

print('#'*60)
# ex 2
def checkName(name):

        return name.startswith('M')

myName = ['Mostafa', 'mohamed', 'Mona', 'Ahmed']

result = filter(checkName , myName)

for n in result:
    print(n)
# ------------------------------------------
print('#'*60)
# ex 3 by lambda
# def checkName(name):

#         return name.startswith('M')

myName = ['Mostafa', 'mohamed', 'Mona', 'Ahmed']

result = filter(lambda name : name.startswith('m') , myName)

for n in result:
    print(n)
print('#'*60)
# -----------------------------------------------
# [1] Reduce(func. , iterator)
# [2] it run func. on first & second element and give result
# [3] then run func. on result & third element , then result & fourth and so on
# [4] till one element left and this is result of reduse
# [5] func. pre-defined or lambda func.
# --------------------------------------------------

from functools import reduce

# def sumAll(num1, num2):
#      return num1 + num2

myNum = [1, 12, 5, 60, 23]

myResult = reduce((lambda num1, num2 : num1 + num2) , myNum) #((((1+12)+5)+60)+23)

print(myResult)
# -----------------------------------------------------------
print('#'*60)
# -----------------------------
# enumerate(iterable , start= 0)

mySkills = ['css','js', 'php', 'python', 'html']

skillsWithCounter = enumerate(mySkills, 1)
for counter , s in skillsWithCounter:
     print(f'[{counter}] - {s}')

# --------------------------------
    #  help(func.)
# ----------------------------
    #  reversed(iterable)
print('#'*60)

for l in reversed(mySkills):
     print(l)