# continue #> stop at current iteration then follow

nums = [1, 2, 3, 5, 11, 13, 17, 19]
for num in nums:
    if num == 13:
        continue #stop at current iteration (13) then follow 
    print(num)
print('#'*60)
# Break >> stop loop 
    
for num in nums:
    if num == 13:
        break 
    print(num)
print('#'*60)

# pass >> 
for num in nums:
    if num == 13:
        pass 
    print(num)
print('#'*60)

# advanced dict by loop
mySkills = {
    'html' : '60%',
    'python' : '90%',
    'css' : '50%',
    'js' : '40%',
    'c#' : '30%',
    'C++' : '70%'
}
for key, value in mySkills.items():
    print(f'{key} => {value}')
print('#'*60)

people = {
    'mostafa' : {
        'html' : '60%',
        'python' : '90%',
    }, 
     'ahmed' : {
        'css' : '50%',
        'js' : '40%',
    },
     'abdo': {
        'c#' : '30%',
        'C++' : '70%' 
    }  
     }
# for person in people:
#     print(f'{person} have ')
    
#     for skill in people[person]:
#         print(f'- {skill} => {people[person][skill]}')

for name_key , name_value in people.items():
    print(f'{name_key} have :')
    for skill_key , skill_value in name_value.items():
        print(f'- {skill_key} => {skill_value}')