# A legnagyobb elem megkeresése.
from random import randint
szamok=[randint(-100,100) for i in range(20)]
print(szamok)

# Maximum kiválasztás tétele

# Melyik a legnagyobb szám


legnagyobb=szamok[0] # azt állítjuk hogy az első elem a legnagyobb

#for szam in szamok: # van benne egy fölösleges vizsgálat(az első elemet önmagával vizsgáljuk)
for szam in szamok[1:]: #kihagyjuk a 1. indexű elemet   
    if szam>legnagyobb:
        legnagyobb=szam
print(f'A legnagyobb szám: {legnagyobb}.') 

# Hányadik a legnagyobb szám? --> ebből azt is tudjuk majd, hogy melyik az
legnagyobb_indexe=0 # feltesszük, hogy a 0. a legnagyobb
for i in range(1,len(szamok)): # a 0. elemet kihagyjuk
    if szamok[i]>szamok[legnagyobb_indexe]:
        legnagyobb_indexe=i
print(f'A legnagyobb szám {szamok[legnagyobb_indexe]}, sorszáma: {legnagyobb_indexe+1}.')

#Hányadik a legnagyobb páratlan szám?
legnagyobb_indexe=len(szamok) # olyan elemet kell belrakni, amit biztosan felül fogunk írni!!!
# szamok[legnagyobb_indexe] #list index out of range
for i in range(len(szamok)): # most a 0. indextől vizsgálódunk
    if szamok[i]%2==1: # csak akkor kerssük a legnagyobbat, ha páratlan
    #    if legnagyobb_indexe==len(szamok): # ha a rossz érték van még benne
    #        legnagyobb_indexe=i
    #    elif szamok[i]>szamok[legnagyobb_indexe]:
    #        legnagyobb_indexe=i
        if legnagyobb_indexe==len(szamok) or szamok[i]>szamok[legnagyobb_indexe]:
            legnagyobb_indexe=i
if legnagyobb_indexe==len(szamok):
    print('Nincs páratlan szám a listában')
else:
     print(f'A legnagyobb páratlan szám {szamok[legnagyobb_indexe]}, sorszáma: {legnagyobb_indexe+1}.')

import math
#Hányadik a legnagyobb páratlan szám? v2
# legnagyobb_indexe=-999999999 olyan elemet kell belerakni, amit biztosan felül fogunk írni
legnagyobb_ertek=-math.inf #végtelen
legnagyobb_indexe=False # hamis - itt logikai érték van benne
for i in range(len(szamok)):
    if szamok[i]%2==1 and szamok[i]>legnagyobb_ertek:
        legnagyobb_ertek=szamok[i]
        legnagyobb_indexe=i    #belekerült egy egész szám!
if legnagyobb_indexe!=False:  # ha van páratlan
     print(f'A legnagyobb páratlan szám {szamok[legnagyobb_indexe]}, sorszáma: {legnagyobb_indexe+1}.')
else:    
    print('Nincs páratlan szám a listában!') 




