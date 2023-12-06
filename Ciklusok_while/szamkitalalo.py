#Generáljunk egy 1 és 100 közé eső számot
# A játékos feladata az, hogy ezt kitalálja.
#Segítség: a tipp kisebb vagy nagyobb a kersett számnál

#from random import randint
#titkos_szam=randint(1,100)
import random
titkos_szam=random.randint(1,100)
#print(titkos_szam) tesztelés miatt írtuk csak ki

tipp=-1
tippek_szama=0 #kezdetben még nem volt tipp

while tipp!=titkos_szam: # addig megy, amig el nem találjuk 
    tipp_txt=input('Tipp (1-100):')
    tippek_szama+=1
    if tipp_txt.isnumeric(): # csak akkor vizsgáljuk, ha pozitív egész szám
        tipp=int(tipp_txt) #egész számmá konvertáljuk
        if tipp>titkos_szam:#ha a tippünk túl nagy
            print('Kisebb!')
        elif tipp<titkos_szam:#ha a tippünk túl kicsi
            print('Nagyobb!')

print(f'Talált, {tippek_szama} tippre volt szükség.')


