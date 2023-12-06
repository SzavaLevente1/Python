#Kérjük be egy másodfoku egyenlet együtthatóit(a,b,c)
#és írjuk ki a gyökeit(megoldásait): x1,x2

from math import sqrt

#Bekérni a,b,c

#megvizsgálni a d-t (b**2-4*a*c) if!!

a=float(input('Kérem az a oldalt: '))
b=float(input('Kérem az b oldalt: '))
c=float(input('Kérem az c oldalt: '))

d=b**2-4*a*c

if d>=0: #van megoldás a valós számok halmazán
    x1=(-b+sqrt(d))/(2*a)
    x2=(-b-sqrt(d))/(2*a)
    print(f'x1 = {x1}')
    print(f'x1 = {x2}')
else:  #nincs van megoldás a valós számok halmazán
    print('Nincs  megoldás a valós számok halmazán')
 



