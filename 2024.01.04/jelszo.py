nev='bori98'
jelszo='Szivecske<4'

while nev!='bori99' and jelszo!='Szivecske<3':
    nev=input('Adja meg a felhasználónevét! ') 
    jelszo=input('Adja meg a jelszavát! ')
    if nev!='bori99' or jelszo!='Szivecske<3':
        print('Belépés megtagadva')
    else:
        print('Belpés engedélyezve')    

