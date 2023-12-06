nevek = ['Nikovits Ádám','Palkovics Marcell','Papp Zsolt','Rákóczy Tamás','Rózsavölgyi Simon','Szabó Benjámin','Száva Levente Imre','Veiger Kevin','Zagyva Tamás','Zalavári Marcell']

def osztalyletszam()->int:
    # Visszaadja a nevek lista hosszát.
    return len(nevek)

def leghosszabb_nev()->str:
    #Visszaadja a leghosszabb nevű diák nevét.(Az első leghoszabbat.) - Maximum kiválasztás
    leghosszabb=nevek[0]
    for nev in nevek[1:]:
        if len(nev)>len(leghosszabb):
            leghosszabb=nev
    return leghosszabb     

def atlag_hossz()->float:
    # Visszadja a nevek átlagos hosszát.
    osszeg=0
    for nev in nevek:
        osszeg+=len(nev)
    return osszeg/osztalyletszam()  # a fgv. meghívja a másik fgv-t

def van_e(keresett_nev:str)->bool:
    # Eldönti, hogy a kersett név benne van-e a listában.
    for nev in nevek:
        if keresett_nev.upper() in nev.upper():
            return True
    return False

def tanulo_szamol(keresett_nev:str)->int:
    # Megszamolja, hogy a kersett név hányszor szerepel a listában?
    darab=0
    for nev in nevek:
        if keresett_nev.upper() in nev.upper():
            darab+=1
    return darab      

def keres(keresett_nev:str)->int|bool:
    # A kersettt nevű tanuló első előfodulásának indexét adja vissza, ha nincs, akkor False értéke.
    for i in range(osztalyletszam()):
        if keresett_nev.lower() in nevek[i].lower(): # Itt is lehetne upper()-t is használni
            return i
    return False   
       