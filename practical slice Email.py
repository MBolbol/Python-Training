# email = 'osama@elzero.org'
# print(email[0:5])
# print(email.index('@'))
# print(email[:email.index('@')])
name = input('what\'s your name?').strip().capitalize()
email = input('what\'s your email?')
userName = email[:email.index('@')]
website = email[email.index('@')+ 1:] #OR email[email.index('@'):].strip('@')
print(f'Hello {name}, your Email is {email}')
print(f'Your user name is: {userName},equivalent to  the website is: {website} ')


# practical your age full details

age = int(input('what\'s your age ?').strip())

months = age * 12
weeks = age * 12 * 4

days = age * 365
# collect time units
unit = input('Please choose time unit : Months, weeks, Days').strip().capitalize()

if unit == 'Months' or unit == 'm' :
    print(f'Your age is {months} Months')

elif unit == 'Weeks' or unit == 'w':
    print(f'Your age is {weeks} weeks')

else:
    print(f'Your age is {days} days')
        

# get age in all time units

# hours = days * 24
# minutes = hours * 60
# seconds = minutes * 60


# print(f'''You lived for: {age} years,
#       equivalent to {months} months,
#       equivalent to {weeks:,} weeks,
#       equivalent to {days:,} days,
#       equivalent to {hours:,} hours,
#       equivalent to {minutes:,} minutes,
#       equivalent to {seconds:,} seconds.''')

# practical year age full details
