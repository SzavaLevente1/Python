# megszamoljuk, hogy hány elem felel meg egy feltételnek

from random import randint

szamok=[]

for i in range(randint(10,40)):   # véletlen-szer fut le (10-40)
    szamok.append(randint(-100,100))

print(szamok)    
# Hány elem van a listában?
print(f'{len(szamok)} darab szám került legenerálásra.')

# Megszámlálás tétele:

# Hány páros szám van a listában
db=0
for szam in szamok:
    if szam%2==0:   # ennek a feltételnek kell mefelelnie az aktuális elemnek
        db+=1  #ha megfelel akkor növeljük a darabszámot
print(f'{db} páros szám van a listában.')        

# Hány negatiív szám van a listában?
db=0
for szam in szamok:
    if szam<0:   # ennek a feltételnek kell mefelelnie az aktuális elemnek
        db+=1  #ha megfelel akkor növeljük a darabszámot
print(f'{db} negatív szám van a listában.')     