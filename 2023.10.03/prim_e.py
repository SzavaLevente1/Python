from math import sqrt

szam=int(input('Írj be egy pozitív egész számot: '))

prim=True #kezdetben azt mondjuk, hogy prím, és ha majd találunk osztót, akkor átállítjuk
for i in range(2,int(sqrt(szam))+1):
    if szam%i==0:  # találtunk egy osztót
        prim=False  # így már nem prímszám

if prim:  # if prim==True
    print('Prím!')
else: 
    print('Nem prím!')