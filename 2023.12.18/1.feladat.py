import math

print('1.feladat: Háromszög kerülete és területe\nKérem a háromszög oldalait')
a=float(input('a = '))
b=float(input('b = '))
c=float(input('c = '))
K=a+b+c
s=K/2
print(f'K = {K}')
T=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f'T = {T}')
