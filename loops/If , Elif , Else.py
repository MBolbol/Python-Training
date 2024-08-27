# control flow ..... make decisions
uName = 'BOLBOL'
uCountry = 'Egypt'
cName = 'python course'
cPrice = 100
isstudent = 'yes'


if uCountry == 'Egypt':
    print(f'Hello {uName} Because you are from {uCountry}')
    
    # Nasted IF
    if isstudent == 'yes':
        print(f'And you are student, The \"{cName}\" price is: ${cPrice - 70}')
    
    else:
        print(f'The \"{cName}\" price is: ${cPrice - 50}')

 

elif uCountry == 'KSA': 
    print(f'Hello {uName} Because you are from {uCountry}')
    print(f'The \"{cName}\" price is: ${cPrice - 20}')

else :

    print(f'Hello {uName} Because you are from {uCountry}')
    print(f'The \"{cName}\" price is: ${cPrice - 30}')

print('=' * 50)
country = 'Egypt'

if country == 'Egypt': print(f'the weather in {country} is 25')

    
elif country == 'KSA': print(f'the weather in {country} is 40')
    

else: print('Country isn\'t in the list')
    
# Ternary conditional operator >> short if

movierate = 18
age = 20

print('=' * 50)

if age < movierate:
    print('Movie is not good 4U')

else:
    print('Movie is good 4U and happy watching')

# short if
# condition if true | if condition | else | condition if false

print('Movie is not good 4U' if age < movierate else 'Movie is good 4U and happy watching')
  
   