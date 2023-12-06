#0 1 1 2 3 5 8 13 21
# A nulladik eleme a 0 az első eleme az 1
# a további elemeket az előző 2 elem összegéből kapjuk
#a(n)=a(n-1)+a(n-2) - akutális=előző+előző elöttki

#Kérjünk be egy n számot és írjuk kia s orozat első n db elemét

n=int(input('Hány elemű legyen a sorozat?: '))

elozo_elotti=0
elozo=1

if n>=2:
    print('0 1 ',end='')
elif n==1:
    print('0')

for i in range(n-2): # pl. 10 elemű sorozatnál (mivel az első 2 eleme megvan) 8 elemet kell kiszámolni
    aktualis=elozo_elotti+elozo
    elozo_elotti=elozo
    elozo=aktualis
    print(aktualis,end=' ')