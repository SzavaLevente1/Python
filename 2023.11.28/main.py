from nobel import *

beolvas('nobel.csv')

print(f'3.feladat: {tipus_nev_alapjan("Arthur B. McDonald")}')

print(f'4.feladat {dijazott_ev_tipus_alapjan(2017,"irodalmi").teljesnev}')

print('5.feladat:')
szervezetek_adott_ev_utan(1990)

print('6.feladat:')
dijazott_nev_tartalmazza('Curie')

print('7.feldat:')
nobeldij_statisztika()