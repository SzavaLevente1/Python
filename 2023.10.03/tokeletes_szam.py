# Tökéletes számok

# Akkor nevezünk egy pozitív egész számot tökéletes számnak, ha a szám önmagánál kisebb osztóinak az összege megegyezik a számmal.
# Kérjünk be egy számot és mondjuk meg, hogy tökéletes szám-e!

szam=int(input('Szám: '))
osszeg=0 # önmagánál kisebb osztók összege (kezdetben 0)
for i in range(1,int(szam/2)+1):
    if szam%i==0: # ha találtunk egy osztót
        osszeg+=i # növeljük az osszeg változót a talált osztóval

if osszeg==szam:
    print('Tökéletes szám!')
else:
    print('Nem tökéletes szám.')