#Adott szám számjegyeinek fordított sorrendjének a meghatározása.(ez bármilyen string fodított kiírásra jó lesz!)

szam=input('Kérek egy számot: ')# ez jelenleg egy string

print(szam) #egyben írjuk kia astringet
print(len(szam))

# for i in range(len(szam)): #123456 esetén range(6)-nak felel meg tehát az i-->0-5-ig veaz fel értéket
#    print(szam[i],end='')#egymás mellé karakterenként
forditott=''
for i in range(len(szam)-1,-1,-1):#a szöveg végétől egyesével megyünk vsszafele az elejéig
    print(szam[i],end='') #karakterenként írjuk ki 
    forditott+=szam[i] #karakterenként beletszzük egy másik változóba(fordítva)

print(f'\n{forditott}') #kiírjuk egyben a másik változót, amiben fordítva van
