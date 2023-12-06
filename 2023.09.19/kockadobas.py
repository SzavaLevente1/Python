#Dobjunk 1 hagyományos dookockával, és számoljuk meg hogy hány 6-os volt

from random import randint

n=20 #kockadobások száma

#ennél lesz jobb megoldásunk később
egyesek_szama=0
kettesek_szama=0
harmasok_szama=0
negyesek_szama=0
otosok_szama=0
hatosok_szama=0

for i in range(n):
    dobas=randint(1,6)
    print(dobas,end=' ')
    # if dobas==1:
    #    egyesek_szama+=1
    # elif dobas==2:
    #    kettesek_szama+=1
    # elif dobas==3:
    #    harmasok_szama+=1
    # elif dobas==4:
    #    negyesek_szama+=1
    # elif dobas==5:
    #    otosok_szama+=1
    # else: 
    #     hatosok_szama+=1
    match dobas: #az aktuális dobás értékét vizsgáljuk
        case 1: egyesek_szama+=1 #case - eset (egy lehetséges)
        case 2: kettesek_szama+=1
        case 3: harmasok_szama+=1 
        case 4: negyesek_szama+=1 
        case 5: otosok_szama+=1
        case 6: hatosok_szama+=1 
        # case _: # akkor fut le, ha a fenti esettek egyike sem teljesül 
  

print(f'\nEgyes dobasok száma: {egyesek_szama}')        
print(f'Kettes dobasok száma: {kettesek_szama}')        
print(f'Hármas dobasok száma: {harmasok_szama}')        
print(f'Négyes dobasok száma: {negyesek_szama}')        
print(f'Ötösö dobasok száma: {otosok_szama}')        
print(f'Hatos dobasok száma: {hatosok_szama}')        