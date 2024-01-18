from functions import *

print('3. feladat: CB-Rádió')
beolvas('cb.txt')

print(f'3.2 feldat: Behjegyzések száma: {bejegyzesek_szama()} db')

print(f'3.3 feldat: Sanyihoz tartozó bejegyzések: {nev_bejegyzesszam("Sanyi")} db')

print('3.4 feladat: A legtöbb adás: ')
for adas in cbAdasok:
    if adas.darab==maxAdasDb():
        print(f'\tIdő: {adas.ora}:{adas.perc} Darab: {adas.darab} Név: {adas.nev}')

fajlbairas('cb2.txt')        