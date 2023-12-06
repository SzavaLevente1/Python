# NÉV:

# 1. Feladat
# Kérjen be a felhasználótól 2 számot (a,b)!
# Generáljon ezen az intervallumon 10 db egész számot! (a-b)
# Számolja meg és írja ki, hogy a generált számok között 
# hány darab olyan szám van, amely osztható 3-mal.

from random import randint

a=int(input('a= '))
b=int(input('b= '))
db=0
for i in range(10):
    szam=randint(a,b)
    print(szam,end=' ')
    if szam%3==0:
        db+=1
print(f'\n{db} db 3-mal osztható szám van a generáltak között.')        


#----------------------------------------------------------

#2. feladat

# Kérje be 3 felhasználó nevét és életkorát.
# Az életkort addig kérje, amíg nem megfelelő értéket kap. (18-99)
# Határozza meg, hogy ki a legidősebb!
print('-------------------------------------')
legidosebb=''
legidosebb_kora=0

for i in range(3):
    kor=-1
    nev=input('Név: ')
    while kor<18 or kor>99:
        kor=int(input(' Kor (18-99): '))
    if kor>legidosebb_kora:
        legidosebb_kora=kor
        legidosebb=nev
print(f'{legidosebb} a legidősebb ({legidosebb_kora} éves)')        
