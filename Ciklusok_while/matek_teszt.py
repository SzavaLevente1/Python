from random import randint

kerdesek_szama=5#csak itt kell átírni, ha többet/bevesebbet szeretnénk

rossz_valaszok_szam=0
for i in range(kerdesek_szama):
    szam1=randint(1,10)
    szam2=randint(1,10)
    muvelet=randint(0,2) # 0='+' 1='-1  2='*'
    helyes_valasz=False #kezdőértéka while ciklushoz

    while helyes_valasz==False:
     match muvelet:
        case 0: #'+'
            valasz=int(input(f'{szam1} + {szam2} = '))
            if szam1+szam2==valasz:
               print('Jó válasz!')
               helyes_valasz=True
            else:
                print('Rossz válasz!')
                rossz_valaszok_szam+=1   
        case 1: #'-'
            valasz=int(input(f'{szam1} - {szam2} = '))
            if szam1-szam2==valasz:
               print('Jó válasz!')
               helyes_valasz=True
            else:
                print('Rossz válasz!')
                rossz_valaszok_szam+=1                      
        case 2: #'*'
            valasz=int(input(f'{szam1} * {szam2} = '))
            if szam1*szam2==valasz:
               print('Jó válasz!')
               helyes_valasz=True
            else:
                print('Rossz válasz!')
                rossz_valaszok_szam+=1
print(f'Eredményesség: {kerdesek_szama/(kerdesek_szama+rossz_valaszok_szam)*100:.2f}%')

#KÉSŐBB függvény használata, mert kb ugyanazt csináltuk 3-szor (3 műveletnél)