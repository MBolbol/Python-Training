# integer >> 15, -12    ,10   ,100
# float >>>> 15.111 ,-100.333
# complex >> 5+6j  ,10-7j
x = 10-7j
print(type(x))
print('real part is: {}'.format(x.real))
print('imaginary part is: {}'.format(x.imag))
# Arithmetic operators
# add (+) , subtraction (-) , multiplication (*) , division (/)
# Modulus (%) باقى القسمة , Exponent (**) اس كذا , Floor division (//) خارج القسمة الصحيح
print(10%2)
print(10//2)
print(10**2)
print('=' * 50)

print(15//2)
print(15/2)
print(15%2)
print('=' * 50)

# Assignment Operators 
# [ = ]
x = 10 
y = 20
z = x + y 
print(z)
print('=' * 50)
# [ += ]
x += y # == (x = x + y) 
print(x)
print('=' * 50)
# [ -= ]
x -= y # == (x = x - y) 30-20 = 10
print(x)
print('=' * 50)
# [ *= ]
x *= y # == (x = x * y)
print(x)
print('=' * 50)
# [ /= ]

# [ **= ]
a = 2
b = 3
a **= b # == (a = a**b)  a power to b 
print(a)
print('=' * 50)

# [ %= ] 
c = 10
d = 3
c %= d # == (c = c % d )  c moduls d 
print(c)
print('=' * 50)

# [ //= ] 
f = 10
g = 3
f //= g # == (f = f // g )  f Floor division g 
print(f)
print('=' * 50)

# Comparison operators
# (==) equal  ,  ( != ) Not equal
print(100 == 100.00)
print(100 == 200)
print(100 != 200)
print('=' * 50)

# ( > ) greater than ,, ( < ) less than
# [ >= ] greater than or equal, [ <= ] less than or equal
print(100 >= 100.00)
print(100 <= 200)
print(100 >= 200)
print('=' * 50)
