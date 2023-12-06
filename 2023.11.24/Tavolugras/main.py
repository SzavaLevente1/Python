from versenyzo import versenyzo

versenyzok:list[versenyzo]=[]

versenyzok.append(versenyzo('Kovács Béla',7.56,8.12,6.45))
versenyzok.append(versenyzo('Gipsz Jakab',6.66,7.12,6.98))
versenyzok.append(versenyzo('Makk Márton',8.01,8.87,7.32))
versenyzok.append(versenyzo('Kiss Albert',6.87,5.65,6.74))

print('      Név         1.      2.      3.   Legnagyobb')
print('-------------------------------------------------')
for egy_versenyzo in versenyzok:
    print(f'{egy_versenyzo.nev.ljust(15," ")}| {egy_versenyzo.elso}  |  {egy_versenyzo.masodik}  |  {egy_versenyzo.harmadik}  |  {egy_versenyzo.legnagyobb_ugras()}')
    print('-------------------------------------------------')

# Hány olyan versenyző vanm akinek midenhárom ugrása 6.5 méter feletti    
mind_hatesfel_feletti=0 # versenyzők száma, akinem minden ugrása 6.5 feletti
for egy_versenyzo in versenyzok:
    if egy_versenyzo.elso>6.5 and egy_versenyzo.masodik>6.5 and egy_versenyzo.harmadik>6.5:
        mind_hatesfel_feletti+=1
print(f'\n\n{mind_hatesfel_feletti} Versenyzőnek nagyobb mindhárom dobása mint 6.5 méter.')
#Ki nyerte a versenyt? és mekkora ugrással?
gyoztes_index=0
for i in range(1, len(versenyzok)):
    if versenyzok[i].legnagyobb_ugras()>versenyzok[gyoztes_index].legnagyobb_ugras():
        #legnagyobb_ugras( - az osztály tagfüggvényének meghívása, mindenképpen kell(, mert az fgv.paraméterlitáját tartalmazza))
        gyoztes_index=i
print(f'Győztes: {versenyzok[gyoztes_index].nev} ({versenyzok[gyoztes_index].legnagyobb_ugras()}m)') 


resztvevo=input('\nKeresett versenyző ')

for egy_versenyzo in versenyzok:
    if egy_versenyzo.nev.upper()==resztvevo.upper():
        print(f'{egy_versenyzo.nev} Legnagyobb ugrása? {egy_versenyzo.legnagyobb_ugras()}')
        break
else:
    print('Nem indult ilyen nevű versenyző!')           