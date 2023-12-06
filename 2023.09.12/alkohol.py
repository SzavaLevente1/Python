#Döntsük el, hogy vehet-e alkoholt a vásárló vagy nem
#Elmúlt-e 18 éves

ma_ev=2023
ma_honap=9
ma_nap=12

szuletes_ev=int(input('Születés éve: '))

if ma_ev-szuletes_ev<18:
    print('Még nincs 18 éves. NEM vehet alkoholt!')
elif ma_ev-szuletes_ev>18: #elif - különben ha... 
    print('Az alkohol öl butít és nyomorba dönt.Ha akar, akkor vehet alkoholt.')
else: #különben ág - pontosan 18 éves az évek alapján
    szuletes_honap=int(input('Születés hónap: '))
    if ma_honap<szuletes_honap:
        print('Még nincs 18 éves. NEM vehet alkoholt!')
    elif ma_honap>szuletes_honap: #elif - különben ha... 
     print('Az alkohol öl butít és nyomorba dönt.Ha akar, akkor vehet alkoholt.')
    else: #különben ág - pontosan 18 éves az évek alapján
        szuletes_nap=int(input('Születés hónap: '))
        if ma_nap<szuletes_nap:
             print('Még nincs 18 éves. NEM vehet alkoholt!')
        elif ma_nap>szuletes_nap: #elif - különben ha...
             print('Az alkohol öl butít és nyomorba dönt.Ha akar, akkor vehet alkoholt.')
        else: #pontosan 18 éves
            print('Boldog születésnapot! Igyon egy pezsgőt!')      
             
     


     
