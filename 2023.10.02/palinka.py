from random import randint

osszesen=0 #kezdetben még nincs pálinka
ivott=False #még csak most kezdi főzni, még biztos, hogy nem iszik haverokkal

for i in range(1,31): #i --> 1..30 (30 nap)
    if ivott==False:  #csak ha nem isziki a haverokkal
        mai_fozet=randint(1,5) # 1-5 l a keletkezett pálinka
        osszesen+=mai_fozet
        if randint(1,5)==5: #20% hogy megisznak 1 liter pálinkát
            ivott=True
            osszesen-=1 #megittak 1 liter páleszt
        print(f'{i}. nap: {mai_fozet} liter eddigi termés összesen: {osszesen} liter. ',end='')
        if ivott: #if ivott==True:
            print('Ma ivott Pista bácsi a haverokkal.',end='')
        print() #sortörésre használjuk 
    else: #ha előző nap ivott
        print(f'{i}. nap: Pista bácsi nem főz, mert másnapos.')
        ivott=False #nap végére kijózanodik teljesen, és újra készen áll a főzésre      

print(f'A 30. nap végére Pista bácsinak {osszesen} liter pálinkája lett')