# for item in iterable_object:
#   do something with item
# -----------------------------
# item is a var you create and call whenever you want
# item refer to current position and will run and visit all items to the end 
# iterable_object => sequance [list, tuple, set, str, dict, etc ... ]
# -------------------------------------

nums = [1, 2, 3 , 4 , 5 , 6 , 7 , 8 , 9]
for i in nums :
    # print(i*3)
    if i % 2 == 0 : #moduls 2 >>even
        
        print(f'the num ({i}) is even nums')
    else:            
        print(f'the num ({i}) is odd nums')
else:
    print('the loop is finished')


n = 'bolbol'
for letter in n :
    print(f'{letter.upper()}')

print('#'*60)
# --------------------
# # range 
# myRange = range(1 , 100)
# for num in myRange : 
#     print(num)

# dict
mySkills = {
    'html' : '60%',
    'python' : '90%',
    'css' : '50%',
    'js' : '40%',
    'c#' : '30%',
    'C++' : '70%'

}
print(mySkills['python'])
print(mySkills.get('js'))
print('#'*60)

for skill in mySkills :
    # print(skill)
    print(f'My progress in {skill} = {mySkills[skill]}')
print('#'*60)

# Nasted loop by for

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

for name in people:
    print(f'Skills and progress for {name} is:')

    for skill in people[name]:
        print(f'{skill.upper()} => {people[name][skill]}')

# skills = ['html','python','css' ]

# for name in people: #outer loop

#     print(f'{name} skills is : ')
# # inner loop
#     for skill in skills :
#         print(skill)