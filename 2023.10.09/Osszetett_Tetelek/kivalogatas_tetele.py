# A feltételnek megfelelő elemeket átplakolja egy másik listába.
#3-mal osztható számok

from random import randint
szamok=[]
for i in range(100):
    szamok.append(randint(-100,100))
print(szamok)

#kiválogatás
harommal_oszthato_szamok=[]
for szam in szamok:
    if szam%3==0:
        harommal_oszthato_szamok.append(szam)

print(f'Hárommal osztható számok:\n{harommal_oszthato_szamok}')


