from HegyekMo import *

beolvas('hegyekMo.txt')

print(f'3.feldat: Hegycsúcsok száma: {len(hegyek)} db')
# print(f'3.feldat: Hegycsúcsok száma: {hegyek_szama()} db') #ha minden fgv-nyel kell megoldani

print(f'4.feadat: hegycsúcsok átlagos maggassága: {atlag_magassag()} m')
# print(f'4.feadat: hegycsúcsok átlagos maggassága: {str(atlag_magassag()).replace(".",",")} m') ha ki akarjuk cserléni a tizedes .-ot ,-re

print(f'5. feladat: A legmagasabb hrgycsúcs adatai:')
legmagasabb=legmagasabb_hegy()
print(f'\tNév:  {legmagasabb.nev}')
print(f'\tHegység: {legmagasabb.hegyseg}')
print(f'\tMagasság:  {legmagasabb.magassag} m')

magassag=int(input('6.feladat: Kérek egy magasságot:'))
if van_magasabb(magassag)==False:
    print(f'\tNincs {magassag} m-nél magassab hegycsúcs.')
else:
        print(f'\tVan {magassag} m-nél magassab hegycsúcs például a(z) {van_magasabb(magassag)}')
 