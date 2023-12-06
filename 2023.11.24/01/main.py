from auto import auto
'''
az_en_autom=auto #példányosítás (obj. példány)
# az_en_autom - objektum, az auto osztály 1 példánya
az_en_autom.rendszam='AA-AA-001'
az_en_autom.szin='kék'
az_en_autom.tipus='Skoda Octavia'
az_en_autom.teljesitmeny=14

'''
autok:list[auto]=[] #az autok egy olyan lista, amelyben auto osztálypéldányok vannak


egy_auto=auto('Skoda','AA-AA-001','kék',140,8.8)
autok.append(egy_auto)
egy_auto=auto('Audi','RRT-787','piros',230)
autok.append(egy_auto)
egy_auto=auto('Lada','AAB-786','barna',45)
autok.append(egy_auto)
egy_auto=auto('KIA','AA-BA-787','zöld',125)
autok.append(egy_auto)

#print(autok[0].teljesitmeny)
#print(autok)
for egy_auto in autok:
    #print(egy_auto.tipus,egy_auto.rendszam,egy_auto.szin,egy_auto.teljesitmeny,egy_auto.gyorsulas )
    print(f'{egy_auto.tipus.ljust(10," ")}{egy_auto.rendszam.ljust(12," ")}{egy_auto.teljesitmeny} LE')
    
    
#legnagyobb teljesitményű autó
legnagyobb_teljesitmenyu_auto=autok[0]
for egy_auto in autok:
    if egy_auto.teljesitmeny>legnagyobb_teljesitmenyu_auto.teljesitmeny:
    # ha az éppen vizsgált autó teljesitménye  nagyobb mint az eddigi legnyagyobb akkor felülirjuk a legnagyobb teljesitményáű autót az éppen vizsgáltal 
     legnagyobb_teljesitmenyu_auto=egy_auto  
    
print('A legnagyobb teljesitményű autó:')
print(f'\tTípusa: {legnagyobb_teljesitmenyu_auto.tipus}')      
print(f'\tRendszama: {legnagyobb_teljesitmenyu_auto.rendszam}')      
print(f'\tSzíne: {legnagyobb_teljesitmenyu_auto.szin}')      
print(f'\tTeljesítménye: {legnagyobb_teljesitmenyu_auto.teljesitmeny}')

# keressünk egy adott remdszámot
bekert_rendzsam=input('\n\n Keresett rendszám: ')
for egy_auto in autok:
    if egy_auto.rendszam.upper()==bekert_rendzsam.upper():
        print(f'\tA kereset autó típus: {egy_auto.tipus}')
        print(f'\tA kereset autó színe: {egy_auto.szin}')
        break
else: #akkor teljesül, ha nem léptünk ki break-kel a ciklusból
    print('\tNincs ilyen autó!')              