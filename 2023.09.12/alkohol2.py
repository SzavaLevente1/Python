ma_ev=2023
ma_honap=9
ma_nap=12

szuletesi_datum=input('Születési dátum( éééé.hh.nn): ')
(szuletesi_ev,szuletesi_honap,szuletesi_nap)=szuletesi_datum.split('.')
#split-string darabolása bizonyos érték mentén/határoló karater/ (a pont karakter)

#számá konvertálás
szuletesi_ev=int(szuletesi_ev)
szuletesi_honap=int(szuletesi_honap)
szuletesi_nap=int(szuletesi_nap)

elmult_18=False #False - hamis, True -igaz
#kezdetben az állítjuk, hogy nem mult el 18

if ma_ev-szuletesi_ev>18:
    elmult_18=True #átbillentjük, mert teljesül a feltétel
elif ma_ev-szuletesi_ev==18:
    if ma_honap>szuletesi_honap:
        elmult_18=True
    elif ma_honap==szuletesi_honap:
        if ma_nap>=szuletesi_nap:
            elmult_18=True
#ha nem teljesül olyan feltételm ahol áttbillentenénk, akkor az erdeti False

if elmult_18==True:
   print('Az alkohol öl butít és nyomorba dönt.Ha akar, akkor vehet alkoholt.')
else:
    print('Még nicsn 18 éves. Nem vehet alkoholt!')


