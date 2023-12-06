#Kerjuk be egy sokszög oldalainak a számát
#Kérjük be egy oldal hosszát
#Írjuk ki a sokszög kerületét!

oldalak_szama=int(input('Adja meg a sokszög oldalanak számát!: '))
kerulet=0
for i in range(oldalak_szama):
    oldal_hossza=int(input('Adja meg az oldal hosszát!: '))
    # kerulet=kerulet+oldal_hossza
    kerulet+=oldal_hossza #kerulet valtozó értékét növeljük az odlal_változó értékével
print(f'Kerület: {kerulet}')    