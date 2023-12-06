# Írjuk ki a prímszámokat egy tartományon!
# Kérjük be a tartomány határait. 
# Figyeljünk arra, hogy a kezdete pozitív szám legyen (>1).
# Figyeljünk arra, hogy a vége nagyobb legyen, mint a kezdete.
from math import sqrt

kezdete=-1
while kezdete<2:
    kezdete=int(input('Kezdete: '))

vege=-1
while vege<=kezdete:
    vege=int(input('Vége: '))

for szam in range(kezdete,vege+1):  # ciklusváltozó lesz a vizsgált szám
    for i in range(2,int(sqrt(szam))+1):
        if szam%i==0:  # találtunk egy osztót
            break
    else: # ha megtaláltuk a prímet, akkor kiírjuk
        print(szam,end=' ')
        
