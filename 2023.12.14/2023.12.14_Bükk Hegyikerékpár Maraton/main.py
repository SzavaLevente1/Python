from functions import *

beolvas('bukkm2019.txt')

print(f'4. feladat: Versenytávot nem teljesítők: {celba_nem_erkezok_aranya()}%')


print(f'5. feladat: Női versenytők száma a rövid távú versenyen: {versenyzokszama("Rövid","Nő")}fő')

# print(f'5. feladat: Férfi versenytők száma a rövid távú versenyen: {versenyzokszama("Hosszú","Férfi")}fő')

if volt_tobb_mint(6*60*60): # 6 óránál volt-e több
    print('6. feldat: Volt ilyen versenytő')
else:
    print('6.feldat: Nem volt ilyen versenyző')
    
print('7. feladat: A felnőtt férfi (ff) kategória győztese rövid távon')
print(f'\tRajtszám: {gyoztes("Rövid","ff").rajtszam}')        
print(f'\tNév: {gyoztes("Rövid","ff").nev}')        
print(f'\tEgyesület: {gyoztes("Rövid","ff").egyesulet}')        
print(f'\tIdő: {gyoztes("Rövid","ff").ido}')        