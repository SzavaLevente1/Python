from tanulo import tanulo
from random import choice, randint
from datetime import datetime

tanulok:list[tanulo]=[] # a tanulo osztalypéldányok kerülnek  bele
vezeteknevek = ['Kiss', 'Kovács', 'Szabó', 'Horváth', 'Fazekas', 'Török', 'Magyar']
keresztnevek = ['Márk', 'Bálint', 'Eszter', 'Judit', 'Elemér', 'Péter', 'Pál', 'Miksa', 'Töhötöm']

def uj_tanuklo() -> tanulo: # visszatérési érték 1 db tanulo (adatai)
    vezeteknev=choice(vezeteknevek)
    keresztnev=choice(keresztnevek)
    szuletesi_ev=randint(2003,2010)
    szuletesi_honap=randint(1,12)
    szuletesi_nap=randint(1,28) # csak azért 28, hogy ne kelljen most ellenőrizni, hogy az adott honaphoz megfelelő-e
    szuletesi_datum=datetime(szuletesi_ev,szuletesi_honap,szuletesi_nap)
    jegyek=[]
    for i in range(randint (0,5)):
        jegyek.append(randint(1,5))
    return tanulo(vezeteknev,keresztnev,szuletesi_datum,jegyek)

def tanulok_feltolt(letszam:int) ->None:
    for i in range(letszam):
        tanulok.append(uj_tanuklo()) #meghivjuk az uj_tanulo(fgv-t) majd a visszatérési értékét (1db tanulo példány) hozzáadjuk a tanulok listához   

def tanulok_kiir() -> None:
    for egytanulo in tanulok:
        print(f'{egytanulo.vezeteknev} {egytanulo.keresztnev} ({egytanulo.szuletes.strftime("%Y.%m.%d.")})')
        print(f'\tJegyei: {egytanulo.jegyek}')
        print(f'\tÁtlaga:{egytanulo.atlag()}') #atlag() tagfüggvény hívása 

def osztaly_legjobja() ->tanulo: #visszatérési érték egy tanulo példány lesz
    legjobb=tanulok[0]
    for egytanulo in tanulok[1:]: # a 0. elemet kihagyva az 1.-től megyünk végig
        if egytanulo.atlag()>legjobb.atlag(): # ha találunk jobb átlagút
            legjobb=egytanulo
    return legjobb # visszaküldjük a legjobb tanuló példányát

def osztaly_atlag() ->float:
    osszeg=0
    for egytanulo in tanulok:
        osszeg+=egytanulo.atlag()
    return osszeg/len(tanulok)

def atlag_folott_letszam() ->int:
    db=0
    for egytanulo in tanulok:
        if egytanulo.atlag()>osztaly_atlag():
            db+=1
    return db            
        
             

        

