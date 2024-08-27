# [1] sequence of char that define a search pattern
# [2] reg exp is not in py only its general concept
# [3] used in [credit card validation, Ip address validation, Email validation]
# [4] test regex 'https://pythex.org/'
# [5] char sheet 'https://www.debuggex.com/cheatsheet/regex/python'
# ----------------------------------------------------------------------
# Quantifiers ----
# --------------------
# * >> (0 or more) 
# + >> (1 or more) 
# ? >> (0 or 1) 
# {2} >> Excatly 2
# {2,5} >> between 2 and 5
# {2,} 2 or more
# {,5} up to 5
# --------------------- 
# Assertions -----
# ^ >> (start of string)
# $ >> (end of string)
# ----------------------------
# match Email
# [A-z0-9\.]+@[A-z]+\.[A-z]+
# [A-z0-9\.]+@[A-z]+\.(com|net|org)$
# ------------------------------------
# Logical or and Escaping ----
# |  >> or
# \  >> escape special char
# () >> separate groups
# ------------------------------------
# Re module -- search and findall --
# search()  => search str for match and return a first match only
# findall() => returns a list of all matches and empty list if no match
# ------------------------------------------------------------------

import re

my_str = re.search('[A-Z]' , 'MostafaBolbol') 
# span = (0, 1) position of str & match only first
print(my_str)
print('#'*60)
my_find = re.findall('[A-Z]' , 'Mostafa Bolbol') 
print(my_find)
print('#'*60)

# ----------------------------------
is_email = re.search(r'([A-z0-9\.]+@[A-z]+\.[A-z]+)', 'mostafa_bolbol@yahoo.com&ahmed_bol@x.com')
print(is_email)
print(is_email.string)
print(is_email.group())
print('#'*60)

# -------------------------------------------
multi_emails = re.findall(r'([A-z0-9\.]+@[A-z]+\.[A-z]+)', 'mostafa_bolbol@yahoo.com&ahmed_bol@x.com')
print(multi_emails)
print('#'*60)
multi_emails = re.findall(r'([A-z0-9\.]+@[A-z]+\.[A-z]+)','')
print(multi_emails)
print('#'*60)

# ---------------------------------------------------------------
# split(pattern, string, Maxsplit) => list of elements splited on each match
# sub(pattern,replace, string, replacecount) => replace matches with what you want
# ----------------------------------------------------------------------
string_one = 'I love python'

my_split = re.split(r' ', string_one, 1)
print(my_split)
print('#'*60)

string_two = 'How-To_Write_A_Very-Good-Article'
search_two = re.split(r'-|_',string_two)
print(search_two)
print('#'*60)
# Get word form URL
for counter , word in enumerate(search_two, 1):
    if len(word) >= 2:

        print(f'({counter}) {word}')
    else:
        # print(f'{word} : is character')
        continue

print('#'*60)

print(re.sub(r'\s', r'_', string_one))
print(re.sub( r'\_|\-',r' ', string_two))

# Flages & Groups
print('#'*60)
