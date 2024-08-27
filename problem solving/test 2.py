# # 33>>37 .... 02 problem
# html = 80 
# css = 60 
# js = 70
# print(html>50 and css>50 and js >50)
# print('#'*60)
# # 03
# num_one = 10
# num_two = 20
# num = 20
# print(num>num_one or num>num_two)
# print(num>num_one and num>num_two)
# print('#'*60)
# # 04
# result = num_one + num_two
# print(result)
# x= result**3
# print(x)
# y = x % 26000
# print(y)
# z = y/5
# print(z)
# print(type(z))
# print(type(str(z)))
# print('#'*60)

# # 38>>40  ,,,,, 02
# age = int(input('How old are you ?').strip())

# if age < 16 :
#     print('Hello your age is under 16, some articles isn\'t suitable for you')
# else:
#     print(f'Hello your age is {age}, all articles is suitable for you')

# print('#'*60)
# # 04
# email = input('Enter your email address, please : ').strip().lower()
# userName = email[:email.index('@')].capitalize()
# site = email[email.index('@') + 1:email.index('.')]
# topDomain = email[email.index('.') + 1:]

# print(f'User name is: {userName}')
# print(f'The site name is: {site}')
# print(f'The Top level Domain is: {topDomain}')
# print('#'*60)

# 41>>>46 ,,,,,,,,01

num1 = int(input('the firs number is : ').strip())
num2 = int(input('the second number is : ').strip())
operation = input('the operation sign is : ').strip()

results = f'{num1} {operation} {num2} ' 
if operation == '+':
    results = int(num1 + num2)
    
    print(f'the result of ({num1} {operation} {num2}) is : {results}')
elif operation == '/':
    results = int(num1 / num2)
    
    print(f'the result of ({num1} {operation} {num2}) is : {results}')

elif operation == '*':
    results = int(num1 * num2)
    
    print(f'the result of ({num1} {operation} {num2}) is : {results}')

elif operation == '-':
    results = int(num1 - num2)
    
    print(f'the result of ({num1} {operation} {num2}) is : {results}')
elif operation == '%':
    results = int(num1 % num2)
    
    print(f'the result of ({num1} {operation} {num2}) is : {results}')
else:
    print('The wrong operation, Sorry')