import datetime
# print(dir(datetime.datetime))
# current date & time
print(datetime.datetime.now())

print('#' *60)
# year
print(datetime.datetime.now().year)
print('#' *60)
# start and end of date
# print(datetime.datetime.min)
# print(datetime.datetime.max)
print('#' *60)
# time
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)
print('#' *60)
# spacific date & time
print(datetime.datetime(1999, 2, 3))
print('#' *60)
# num of days i lived for
myBirthDay = datetime.datetime(1999, 2, 3) 
now  = datetime.datetime.now()

print(f'I lived for {(now - myBirthDay).days} days.')
print('#' *60)

# --------------------------
# format date and time
# month
print(myBirthDay.strftime('%B'))
print(myBirthDay.strftime('%b'))
# day
print(myBirthDay.strftime('%a'))
print(myBirthDay.strftime('%A'))
# date 
print('#' *60)

print(myBirthDay.strftime('%d - %B - %y'))
print(myBirthDay.strftime('%d/%B/%Y'))


