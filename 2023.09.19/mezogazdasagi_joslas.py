#Készítsen programot, amely mezőgazdasági jóslást végez!
#Kérje be az elvetett búza mennyiségét tonnában!
#Ez alapján számolja ki egy véletlenszerűen generált szorzóval (5-15) a hozamot és írja ki a mennyiséget!
#A szorzó alapján határozza meg és írja ki, hogy milyen volt az adott év: 
# 5-8 --> átlag alatti
# 9-12 --> átlagos
# 13-15 --> átlag feletti

from random import randint

t=int(input('Kérem a búza mennyiségét '))
szorzo=randint(5,15)
print(f'Várható menyiség {t*szorzo}')

if szorzo<=8:
    print('A termés átlag alatti.')
elif szorzo<=212:
    print('A termés mennyisége átlagos')
else:
    print('A termés mennyisége átalg feletti')    
      

     
    


    

    
