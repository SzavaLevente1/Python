from functions import *

beolvasas('ub2017egyeni.txt')
print(f'3.2 feladat: Futók száma: {versenyzoszam()}')

print(f'3.3 feladat: Célba érkező női sportolók: {noi_teljes()} fő')

print('3.4 feladat: A leghhosszabb nevű futó')
print(f'\tNév: {leghosszabb_nev().nev}')
print(f'\tRajtszám: {leghosszabb_nev().rajtszam}')
print(f'\tEredemény: {leghosszabb_nev().ido}')

print(f'3.5 Férfi sportolók átlagos ideje: {atlag()} óra ')