# Mire használjuk a függvényeket?
# - Olyan kis program egységek, melyeket változtos bemeneti adatokkal szeretnénk végrehajtani, akár sokszor felhasználva. Cél az újrasznosítás is!
# Mit kell tudnunk a függvényekről:
# - mit csinál a függvény (fontos a függvény neve, utaljon a megvalósított feladatra)
# - mi a paraméterlistája (a fgv. neve után zárójelben megadott, vesszővel eválasztott változó(k))
#      - formális paraméterek (a fgv. deklarációjakor zárójelben felsorolt változók, amiket a fgv kap)
#     -aktuális paraméterek (a fgv. hívásakor fgv-nek adott érték /lehet: konstans, változó, kifejezés,.../)
#     -mit ad vissza a fgv. (return kulcsszó után megadott érték)   
# -meghíváskor a visszadaot érték (return utáni) behelyettesítődik a fgv. helyére
# - a fgv. csak meghíváskor fut le, deklarációkor csak létrejön

#def osszeg(a,b):  # a és b formális paraméterek, csak fgv-en belül lehet használni
def osszeg(a:float,b:float) -> float: #tudunk típusos megadást is 
    #print(a+b) nem kiírni szeretnénk, hanem viszaadni
    return a+b
    # ami a return után van az nem fut le!!!
    print('Ezt soha nem látjuk!') 



print('Összeg: ',osszeg(2,3)) # 2, 3 aktuális paramáéterek

x=float(input('Első szám:'))
y=float(input('Második szám:'))
print(f'{x}+{y}={osszeg(x,y)}') # x,y aktuális paraméterek