# NÉV:Száva Levente Imre

# 1. Feladat
# Kérjen be a felhasználótól 2 számot (a,b)!
# A második számot addig kérje be, amíg mindenképpen
# legyen legalább 100-zal nagyobb az első számnál. (ellenőrzés)
# Generáljon ezen az intervallumon 10 db egész számot! (a-b)
# Számolja meg és írja ki, hogy a generált számok között 
# hány darab olyan szám van, amely 7-tel osztható.
#----------------------------------------------------------

#2. feladat

# Kérje be 3 felhasználó nevét és magasságát (cm), testsúlyát (kg).
# Az magasság és súly adatokat addig kérje be, 
# amíg nem megfelelő értéket kap. (100-220cm/40-200 kg) (ellenőrzés)
# Határozza meg, ki a legmagasabb, és ki a legnehezebb!


# 1 feladat:
a=int(input("Kérem az a számot: "))
b=int(input("Kérem a b számot: "))

while a > b+100:
 print("A szám nem 100-al nagyobb az első számnál")
else:
      print("A szám jó")



# 2 feladat:

felasznalo_1_magassag=int(input("Kérem az első felhasználó magasságát"))
felasznalo_1_suly=int(input("Kérem a első felhasználó súlyát"))
felasznalo_2_magassag=int(input("Kérem a második felhasználó magasságát"))
felasznalo_2_suly=int(input("Kérem a második felhasználó súlyát"))
felasznalo_3_magassag=int(input("Kérem a harmadik felhasználó magasságát"))
felasznalo_3_suly=int(input("Kérem a harmadik felhasználó súlyát"))

if felasznalo_1_magassag and felasznalo_2_magassag and felasznalo_2_magassag <100-220:
     print("Az érték nem jó")
else:
   ("jó értéket addot meg")      

