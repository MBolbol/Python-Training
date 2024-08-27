# n = int(input(' ').strip())

# if n % 2 == 1:
#     print('Weird')
# if n % 2 == 0:
#     if n in range(2,6):
#         print('Not Weird')
#     if n in range(6,21):
#         print('Weird')
#     if n > 20:
#         print('Not Weird')
        
# # ---------------------------------------
# print('#' * 60)
# a = int(input())
# b = int(input())

# x = a + b
# print(int(x))

# y = a - b  
# print(int(y))

# z = a * b
# print(int(z))
# -----------------------------------------
# n = int(input())
# i = range(0, n)

# if n in range(0, 21) :
#         for x in i:
            
#             print(x**2)

# ----------------------------
# def is_leap(year):
#     leap = False
#     x = leap
#     if year in range(1900, 10**5):
#     # Write your logic here
#         if (year % 4 != 0) and (year % 100 == 0) :
#             x = leap

#         if (year % 4  == 0) and (year % 400 == 0) :
#             x = not leap


#         return x

# year = int(input())
# print(is_leap(year))

# def is_leap(year):
#     leap = False
    
#     # if year in range(1900, 10**5):
#     # Write your logic here
#     if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0) :
#         leap = True

#     else:
#         leap = False

#     return leap

# year = int(input())
# print(is_leap(year))
# ----------------------------
# n = int(input())
# # x = list(range(1, n+1))
# # i, = str(range(1, n+1))
# for i in range(1,n+1) :

#     print(i, end='')

# --------------------------------------------------
#  returns the second highest score, which is the runner-up score.

# n = int(input())
# arr = map(int, input().split())

# # if n == (max(arr) - 1) or (n in range(2,10)): 
# #     print(n)
# print(sorted(list(set(arr)))[-2]) # because set don't allow to dublicated (repeated) elements
# -----------------------------------------------------------------------
x = int(input())
y = int(input())
z = int(input())
n = int(input())

if (x in range(0,n+1)) and (y in range(0,n+1)) and (z in range(0,n+1)) :

    print(list(x), end= ',')
    print(list(y), end= ',')
    print(list(z))


