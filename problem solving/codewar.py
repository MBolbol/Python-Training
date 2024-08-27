def temple_strings(obj, feature): 
    print(f'{obj} are {feature}')
    pass

temple_strings("Animals","Good")

# ------------
# How old will be in 2099?
# age = int()
# year_of_birth = int()
# current_year = int()

def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    if int(age) > 0:
        print(f'Your are {age:d} years old')

    if int(age) < 0:
        print(f'you will be born in {age*-1:d} years')

    if int(age) == 0:
        print(f'you were born this very year!')


calculate_age(1999, 2099)