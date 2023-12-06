from autok import *
from os import system

autok_betolt()

while True:
    system('cls') #képernyő törlése
    print('0. kilépés')
    print('1. autó új adatainaki megadása')
    print('2 adatok listázása')
    print('3. A legerősebb autó' )
    print('4. adott színű autók listázása')
    valasztas=input('Választás')

    match valasztas:
        case  '0':
            break
        case '1':
            system('cls')
            auto_beker()    
        case '2':    
            system('cls')    
            print('A nyivlántartásban lévő autok:')
            autok_kiir(autok)
            input('Tovabb...')
        case '3':
            system('cls')
            legerosebb_auto=legerosebb()
            print('A legerősebb autó adatai:')
            print(f'\tRendszám:{legerosebb_auto.rendszam}')    
            print(f'\tTípus:{legerosebb_auto.tipus}')    
            print(f'\tMárka:{legerosebb_auto.marka}')    
            print(f'\tSzín:{legerosebb_auto.szin}')    
            print(f'\tTeljesítmémy:{legerosebb_auto.teljesitmeny}')
            input('Tovabb...')
        case '4':
            system('cls')
            szin=input('Milyen színű autókat listázunk?')
            print(f'{szin} szinű autók: ')
            autok_kiir(autok_szin_alapjan(szin))
            input('Tovabb...')    

                
            