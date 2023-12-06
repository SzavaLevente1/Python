from hegycsucs import hegycsucs

hegyek:list[hegycsucs]=[]

def beolvas(fajlnev):
    fajl=open(fajlnev,'r',encoding='utf-8')
    a=fajl.readline()
    for sor in fajl:
        hegyek.append(hegycsucs(sor.strip()))
    fajl.close()
    
def hegyek_szama(): #ha mindent fgv-el kell megoldani
    return len(hegyek)

def atlag_magassag()->float:
    osszeg=0
    for h in hegyek:
        osszeg+=h.magassag
    return osszeg/hegyek_szama() # lehet len(heygek) is

def legmagasabb_hegy() ->hegycsucs: #visszaad egy pédányt
    legmagasabb=hegyek[0]
    for h in hegyek[1:]:
        if h.magassag>legmagasabb.magassag:
            legmagasabb=h
    return legmagasabb

def van_magasabb(magassag)->bool|str:
    for h in hegyek:
        if h.magassag>magassag:
            return h.nev
    return False     
                     
    
            
         