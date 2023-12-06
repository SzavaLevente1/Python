#Készítsünk programot, amely bekér egy számot,majd hazározza, hogy az a szám négyzetszám-e


from math import sqrt

szam=int(input('Kérem adjon meg egy számot:'))
gyok=sqrt(szam) # a szám négyzetgyöke

if gyok==round(gyok): #a kerekített == az erdetivel --> CSAK ha egész
    print('Négyzetszám!')
else:
    print('NEM négyszetszám!')    