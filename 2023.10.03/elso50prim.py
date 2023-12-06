# írjuk ki az első 50 db prímszámot!
from math import sqrt

db=0 # kezdetben még nem találtuk prímszámot
szam=2 # az első szám, amit vizsgálunk

while db<50: # addig megy, amíg nincs meg az első 50 prím
    for i in range(2,int(sqrt(szam))+1):
        if szam%i==0:  # találtunk egy osztót
            break
    else: # ha megtaláltuk, akkor kiírjuk
        print(szam,end=' ')
        db+=1 # növeljük a megtalált prímek számát
    szam+=1 # lépünk a következő vizsgált számra       