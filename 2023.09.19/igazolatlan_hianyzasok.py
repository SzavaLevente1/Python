# Készítsünk porgramot, amely beolavassa egy diák igazolatlan hiányzásainak számát.
#Készítsünk kategóriákat a hiányzások száma alapján
# 1-5 ofői feigylemeztetés
# 6-10 ofői intő
#11-35 igazgatói megrovás
#35 fölött, kérjük a tanuló születési évét
# ha elmúlt 16, akkor kirúgás (már nem tanköteles)
#egyébként családi pótlék megvonás.

aktuális_ev=2023

# be kell kérni a hiányzások számát

igazolatlan_ora=int(input('Igazolatlan óra száma: '))
if igazolatlan_ora==0:
   print('Nice')
elif igazolatlan_ora<=5:
  print('ofői feigylemeztetés')
elif igazolatlan_ora<=10:
  print('ofői intő')
elif igazolatlan_ora<=35:
  print('igazgatói megrovás')
elif igazolatlan_ora>35:
    kor=int(input('Adja meg a születési évét'))
    kirugas=aktuális_ev-kor
    if kirugas<=16:
     print('Nincs pótlék')
    else:
      print('Emlúlt 16 nem tanköteles')
       
   
    
  