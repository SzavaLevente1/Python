from random import randint

szamok=[]

# lista feltöltése (db,min,max)
def feltolt(n:int,min:int,max:int)->None:
    for i in range(n):
        szamok.append(randint(min,max))

#Eldönt, hogy van-e olyan szám a listában, amely az osztóval maradék nékül osztható.
def van_e_oszthato(oszto:int)->bool:
    for szam in szamok:
        if szam%oszto==0:  #találtunk osztatót
            return True
    return False

# A számok lista elemeinek átlagát adja vissza.
def atlag()->float:
    osszeg=0
    for szam in szamok:
        osszeg+=szam
    return osszeg/len(szamok)

#Megekeresi a paraméterben megadott számot a listában
# Visszaadja a kersett szám nindexét, illetve False-t, ha nincs benne

def keres(mit:int)->int|bool: # int vagy bool visszatérési érték
        for i in range(len(szamok)):
             if mit==szamok[i]:
                  return i
        return False

#Megszámolja, hogy hány olyan elem van a listában, amely egy megadott limitnél nagyobb vagy egyenlő.


def darab_ha_több(limit:int)->int:
    darab=0
    for szam in szamok:
        if szam>=limit:
            darab+=1
    return darab 

