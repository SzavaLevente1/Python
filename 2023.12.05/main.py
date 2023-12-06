from varosok import *

beolvas('varosok.txt')

print(f'3. feladat: Városok száma: {len(varosok)} db')

print(f'4. feladat: indiai nagyárosok lakosságának összege: {orszag_lagossaga("India")} fő')

legnagyobb=legnagyobb_varos()
print(f'5. feladat: A legnagyobb város adatai:')
print(f'\tNév: {legnagyobb.varos}')
print(f'\tOrszág: {legnagyobb.orszag}')
print(f'\tLakosság: {legnagyobb.lakossag} ezer fő')

if orszag_keres('Magyarország'):
    print(f'6. feladat: Van magyar város az adatok között.')
else:    
    print(f'6. feladat: Nincs magyar város az adatok között.')
    
print(f'7.feadat: Városok egy szóközzel: {szokozos_varosok(1)} db')    
print(f'7.1 feadat: Városok kettő szóközzel: {szokozos_varosok(2)} db')    
print(f'7.2 feadat: Egy szóból álló városnevek: {szokozos_varosok(0)} db') 

print('8.feladat: Ország statisztika')
for key,value in orszag_statisztika().items():
    if value>6:
       print(f'\t{key} - {value} db')

print('9. feladat: kina.txt')
orszag_mentes('kina.txt','Kína')          