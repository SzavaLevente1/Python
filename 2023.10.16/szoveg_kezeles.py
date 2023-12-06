mondat = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quibusdam necessitatibus fugiat iure dolorum dicta, delectus distinctio aperiam beatae eveniet fuga ab iusto minima sit labore asperiores eum placeat, praesentium tempora?'
rovid_mondat = 'Lorem ipsum dolor sit amet consectetur adipisicing.'

# Milyen hosszú a mondat(karakterek száma)
print(f'A mondat{len(mondat)} karkterből áll')

#Milyen szóból áll a mondat? (Szóközök száma +1)
darab=0 # kezdetben még nincs szóköz
# for i in range {len(mondat)}:
for karakter in mondat:
    if karakter ==' ':
        darab=+1
print(f'A mondat {darab+1} szóból áll')

# Hány olyan szó van a mondatban, amely legalább 10 karakter hosszú?
darab=0
szo_hossza=0
for karakter in rovid_mondat:
    if karakter!=' ':
        szo_hossza+=1
    else:
        if szo_hossza>=10:
          darab+=1
        szo_hossza=0
if szo_hossza>=10: # az utolsó szó hosszát is meg kell néznünk, aminek nics szóköz a végén, de a ciklus már végigmen a teljes szövegen
    darab+=1
print(f'A mondatban {darab} darab legalább 10 karakter hosszú szó van.')

# v2:
szavak=rovid_mondat.split() # szétdaraboljuk a szöveget és egy listába tesszük a darabokat (szavakat). split() paraméter nélkül a szókösz mentén  darabol
darab=0
for szo in szavak:
    if len(szo)>=10:
      darab+=1
print(f'A mondatban {darab} darab legalább 10 karakter hosszú szó van')

#Kérjünk be egy karaktert, és mondjuk meg, hogy hány darab van belőle a mondatban!(Ne számítson, hogy kicsi vagy nagy betű!)
darab=0
bekert_karakter=input('Karakter: ')
for karakter in mondat:
    if karakter.lower()==bekert_karakter.lower(): # .lower() kisbetűssé konvertál .upper() nagybetűssé konvertál
        darab+=1
print(f'"{bekert_karakter}" karakterek száma a mondatban: {darab}.')

#Melyik karakterből mennyi van? (Karakter statisztika.)

lehetseges_karakterek='qwertzuiopőúasdfghjkléáűíyxcvbnm'
karakter_szama=[]

for lehetseges_karakter in lehetseges_karakterek:
    darab=0
    for karakter in mondat:
        if karakter.lower()==lehetseges_karakter:
            darab+=1
    karakter_szama.append(darab)
#print(karakter_szama)
print('Karakter statisztika:')
for i in range(len(lehetseges_karakterek)):
    print(f'{lehetseges_karakterek[i]}: {karakter_szama[i]}')  

#Melyik karakterből van a legtöbb? (előző feladatra épül)

max_index=0 # kezdetben azt mondjuk, ohgy a 0. inxdexű elem a legnagyobb
for i in range(1,len(karakter_szama)):
    if karakter_szama[i]>karakter_szama[max_index]:
        max_index=i
print(f'A(z) "{lehetseges_karakterek[max_index]}" karakterből van a legtöbb: {karakter_szama[max_index]} db.')            


