# A bekérést addig ismételjük amedig a név helyére üres karakterláncot nem ad meg a felhasználó (csak ENTERt üt)

nev='na'
while nev!='': #amikor üres string a név, akkor lesz vége
    nev=input('Név (ENTER = kilépés): ')
    if nev!='':
        osztaly=input('Osztály: ')
        kategoria=int(input('Kategória: '))
        koltseg=int(int(input('Költésg: ')))

        limit=kategoria*10000

        if koltseg>limit:
            print(f'{nev}: {koltseg-limit} Ft')
        else:
            print(f'{nev}: nincs önköltség')    
