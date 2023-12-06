#Unio: összepaokljuk az elemeket egy közös listába

from random import randint

szamok1=[]
szamok2=[]

for i in range(100):
    szamok1.append(randint(-100,100))
    szamok2.append(randint(-100,100))
print('Szamok 1: ',szamok1)
print('Szamok 2: ',szamok2)

#unio
unio=[]
for szam in szamok1:
    unio.append(szam)
for szam in szamok2:
    unio.append(szam)
print('Unio: ',unio)    