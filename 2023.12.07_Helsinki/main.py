from helsinki import *

beolvas('helsinki.txt')

print(f'3.feladat:\nPontzerző helyezések száma: {pontszerzo_helyezesek_szama()}')

print('4. feladat:')
print(f'Arany: {helyezesek_szama(1)}')
print(f'Ezüst: {helyezesek_szama(2)}')
print(f'Bronz: {helyezesek_szama(3)}')
print(f'Összesen: {helyezesek_szama(1)+helyezesek_szama(2)+helyezesek_szama(3)}')

print(f'5. feladat:\nOlimpiai pontok száma: {olimpiai_pontok_osszege()}')

print('6. feladat:')
uszas=ermek_szama('uszas')
torna=ermek_szama('torna')
if uszas==torna:
    print('Egyenló volt az érmek száma')
elif torna>uszas:
    print('Torna sportágban szereztek több érmet')
else:
     print('Uszás sportágban szereztek több érmet') 
     
mentes('helsinki2.txt')            