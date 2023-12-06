# Kérjük be egy kúp alapjának sugarát és a magasságát(valós)
# Írjuk ki a kúp felszínét és térfogatát

from math import sqrt, pow, pi
#sqrt- négyzetgyök
#pow - hatványozás
# pi - pi (kb3.14)

r=float(input('Adja meg a kúp alapjának sugarát!: '))
h=float(input('Adja meg a kúp magasságát!: '))

#a=sqrt(r**2+h**2)
a=sqrt(pow(r,2)+pow(h,2)) #pow(mit, hányadik hatványra)

A=round(r**2*pi+pi*r*a,2) #teljes felszín (alap+palást)
                          #round(mit, hány tizedes pontossággal)
print(f'A kúp felszíne: {A}')                          

V=pi*r*2*h/3
# V=(pi*r**2*h)/3

print(f'A kúp térfogata: {V:.2f}')