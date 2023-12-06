from nevsor import osztalyletszam,leghosszabb_nev,atlag_hossz,van_e,tanulo_szamol,keres

#Hány ember van a z osztályban
print(f'Az osztályban {osztalyletszam()} fő van.')

# Ki a leghosszabb nevű diák?
print(f'A legosszabb nevű diák: {leghosszabb_nev()}')

#Átlagosan milyaen hosszú egy név az oszztályban
print(f'Az osztály  a nevek átlagos hossza:{atlag_hossz()}')

# Van- e az osztályban 'keresett' neű tanuló?
# Ha van, akkor mennyi?
# Ha van, akkor hányadik a névsorban?
keresett=input('Keresett tanuló neve: ')
if van_e(keresett): #ha van keresett nevű tanulo
    print(f'Van {keresett} az osztályban, {tanulo_szamol(keresett)} fő.')
    print(f'A névsorban az első {keresett} sorszáma: {keres(keresett)+1}')
else:
    print(f'Nincs {keresett} nevű tanuló az osztályban.')