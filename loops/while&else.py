# loop >>while 
# while condition is >> true
# code will run until become false

# a =0
# while a<10 : # condition is true
#     print(a)
#     a += 1
# else: # condition is false
#     print('loop is done')

# while False:
#     print('will not print')
# friends = ['Mostafa','Bolbol',"Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# a = 0
# while a < len(friends) :
#     print(f'# {a+1}, {friends[a]}')
#     a += 1

# print('#'*60)
# # simple bookmark manager

# # empty list to fill later
# myFavouriteWebs = []

# # maximum allowed websites
# maximumWebs = 5

# while maximumWebs > 0 :

# # input new web 
#     web = input('website name without https:// ').strip().lower()
#     # add new website to list
#     myFavouriteWebs.append(f'https://{web}')
# # decrease 1 from allowed websits
#     maximumWebs -= 1
#     print(f'Website added, {maximumWebs} places left')
#     print(myFavouriteWebs)
# else:
#     print('Bookmark is full, you can\'t add more ')
    
# print('#'*60)
# # check if list not empty
# if len(myFavouriteWebs)>0 :

#     # sort list
#     myFavouriteWebs.sort()
#     x = 0
#     print('printing the list of websites in your bookmark')
    
#     while x < len(myFavouriteWebs):
#        print('#'*60)
#        print(myFavouriteWebs[x])
#        x += 1

# simple password guess
tries = 3

mainPassword = 'bolbol123'
inputPassword = input('Enter your password: ')

while inputPassword != mainPassword :
    
    tries -= 1

    print(f'invalid password, please try again, { "last" if tries == 0 else tries  } chances left')

    inputPassword = input('Enter your password: ')

    if tries == 0:
        print('sorry, you input wrong password 3 times, try again later')
        break
else:
    print('correct password')
# else:

        # 




