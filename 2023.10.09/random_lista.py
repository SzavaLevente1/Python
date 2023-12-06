from random import randint

darab=int(input('Hány elemű legyen a lista: '))

szamok=[] #üres lista létrehozása

for i in range(darab):
    szamok.append(randint(10,99)) # az új elemet a lista végére teszi

print(szamok)

# szamok.clear # lista kiürítése
# print(szamok)

szamok.insert(0,1) # az első paraméterben megadott helyre beszúrja a második paraméterben megadott értéket
print(szamok)

szam=szamok.pop() # a lista utolsó elemét veszi ki a listából, és visszaadja a 'szam' változóba(mindha egy verem adatszerkezet lenne) 
print(szam) # kiírjuk, hogy mi volt ez a kivett érték
print(szamok)

szam=szamok.pop(0) # a lista első elemét veszi ki a listából, és visszaadja a 'szam' változóba(mindha egy sor adatszerkezet lenne) 
print(szam) # kiírjuk, hogy mi volt ez a kivett érték
print(szamok)

torlendo=int(input('Mit szeretne törölni: '))
szamok.remove(torlendo) # a megadott elem első előfordulását törli a listából, ha nincs ilyen elem akkor hibaüzenetet kapunk!
print(szamok)