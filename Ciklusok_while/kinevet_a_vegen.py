# Pálya 100 lépés hosszú
# csak 6-os dobással lehet elindulni
# csak pontos dobással lehet célba érni
# Hány dobás kellett, hogy célba érjünk?

from random import randint

dobasok_szama=0
aktualis_mezo=0

while aktualis_mezo<100:
    dobas=randint(1,6)
    dobasok_szama+=1
    if (aktualis_mezo==0 and dobas==6) or (aktualis_mezo>0 and aktualis_mezo+dobas<=100):
        # első része: még nem indultunk el, de 6-ot dobtunk
        # második része: már elindultunk, és az aktuális+ a dobás <=100
        aktualis_mezo+=dobas
    print(f'Dobás értéke: {dobas}. Aktuális mező: {aktualis_mezo}')
print(f'{dobasok_szama} dobással ért célba.')        

