from szamok_modul import szamok,feltolt,van_e_oszthato,atlag,keres,darab_ha_több

feltolt(10,1,100)
# print(szamok) #teljes lista kiírása(tesztelési céllal)
# for szam in szamok:      #lista elemei szóközzel elválasztva
#     print(szam,end=' ')

for i in range(len(szamok)):  #lista elemei veszzővel elválasztva
    print(szamok[i],end='')   # az utolsó elem után nincs vessző! 
    if i<len(szamok)-1:
        print(', ', end='')

oszto=int(input('\n Milyen osztót keressünk?: '))
print(van_e_oszthato(oszto))
if van_e_oszthato(oszto):
    print(f'Van olyan szám a listában, amely osztható ezzel: {oszto}')
else:
    print(f'Nincs olyan szám a listában, amely osztható ezzel: {oszto}')   

# szamok_atlaga=atlag()
# print(f'A lista elemeinek átlaga: {szamok_atlaga}')   
# Ha késöbb nem kell átlag értéke sehol, akkor nem kell eeltárolni

print(f'A lista elemeinek átlaga: {atlag()}') # itt nincs eltárolva

keresett_szam=int(input('keresett szám: '))
kereses_eremenye=keres(keresett_szam)
if kereses_eremenye==False:
    print('A keresett szám nincs a listában')
else:
    print(f'A kersett szám első előfodulásának sorszáma sorszáma: {kereses_eremenye+1}')

print(f'A szám között {darab_ha_több(50)} darab 50-nél nagyob (vagy egyenlő) szám van. ')    
