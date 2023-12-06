#feldobunk egy pénzérmét 100-szor, és mondjuk meg, hogy fej vagy írás volt-e többször!

#0 - fej
#1 - írás

from random import randint
fej = 0
iras = 1 #csak ha külön is zeretnénk számolni, de itt nem közelező,mert ami nem fej, az írás lesz

for i in range(100):
    dobas=randint(0,1) #0-fej, 1-írás
    if dobas==0:
        #   print(dobas,end=' ') kipróbálás tesztelés
          fej+=1  
    else: # csak ha külön is szeretnénk
         iras+=1

print(f'Fejek száma:{fej}, írások száma:{iras}')
# print(f'Fejek száma: {fej}, Írások száma {100-fej}')

    