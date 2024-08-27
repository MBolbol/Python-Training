# \:back slash > escape ch
# \b => back space
print('mostafaa\b bolbol')

# \ => escape new line + '\'
# \\ => escape back slash 
print("hello \
I love \
python")

# \' => escape single quote
print('l love my club \'Ahly\'')

# \n => line feed char >>>new line
print('my name \nmy number \nmy address')

#  \r => carriage return
print('123456\rabcd')

# \t => horizontal tab
print("mostafa\tbolbol")

# \xhh =>char hex value
#########################################
# concatenations 
msg ='I love'
lang = 'python'
print(msg + ' ' + lang )

print('#'*60)
##############################################################
# Membership operators
# in & not in
n = 'mostafa'
print('o' in n)
print('i' in n)
print('#'*60)

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print("Ali" in friends)
print('mostafa' in friends)
print('Abdo' not in friends)

print('#'*60)

# in conditions
countriesOne = ['Egypt' , 'KSA', 'kuwait', 'Oman']
countriesOneDiscount = 80

countriesTwo = ['Germany', 'Italy' , 'USA']
countriesTwoDiscount = 50

myCountry = input('What\'s Your Country? ').strip().capitalize()

if myCountry in countriesOne :
    print(f'Hello you have a discount = {countriesOneDiscount}%')

elif myCountry in countriesTwo :
    print(f'Hello you have a discount = {countriesTwoDiscount}%')

else: print('Sorry, You don\'t have any discount ')
print('#'*60)

# practical Membership control
# list contain admins 

admins = ['Mostafa',"Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# login
name = input('Please type your name : ').strip().capitalize()

if name in admins :

    print(f'Hello {name}, Welcome back ')

    option = input('Delete or Update your name : ').strip().capitalize()
    
    if option == 'Update' or option == 'U':
        theNewName = input('Your new name is : ').strip().capitalize()
        admins[admins.index(name)] = theNewName
        print('Name updated')
        print(admins)
    
    elif option == 'Delete' or option == 'D' :
        admins.remove(name)
        print('name deleted')
        print(admins)
    
    else:
        print('wrong option choosed')

else:
    status = input('Not admin, add you? Yes or NO ').strip().capitalize()

    if status == 'Yes' or status == 'Y':
        admins.append(name)
        print('name added')
        print(admins)

    else :
        print('you are not added.')