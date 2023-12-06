from tanulok import *

tanulok_feltolt(10)
tanulok_kiir()

legjobb_tanulo=osztaly_legjobja()
print(f'A legjobb tanulo: {legjobb_tanulo.vezeteknev} {legjobb_tanulo.keresztnev} Átlag: {legjobb_tanulo.atlag()}')
print(f'Az osztály átlaga: {osztaly_atlag()}')
print(f'{atlag_folott_letszam()} tanuló van az osztlyátlag fölött.')