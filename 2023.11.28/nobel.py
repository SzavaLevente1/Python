from dijazott import dijazott

dijazottak:list[dijazott]=[]

def beolvas(fajlnev):
    fajl=open(fajlnev,'r',encoding='utf8')
    fajl.readline() # címsor kiagyása
    for sor in fajl:
        uj_dijazott=dijazott(sor.strip()) # új osztálypéldány létrehozása a konstruktror meghívásával
        dijazottak.append(uj_dijazott) # új díjazottat hozzáadjuk a listához
    fajl.close

def tipus_nev_alapjan(nev:str)->str:
    for d in dijazottak:
        if nev.upper()==d.teljesnev.upper():
            return d.tipus
    return None 

def dijazott_ev_tipus_alapjan(ev:int,tipus:str):
    for d in dijazottak:
        if ev==d.ev and tipus==d.tipus:
            return d 
    return None

def szervezetek_adott_ev_utan(ev:int):
    for d in dijazottak:
        if d.ev>=ev and d.vezeteknev=='':
            print(f'\t{d.ev}: {d.keresztnev}')

def dijazott_nev_tartalmazza(nev:str):
    for d in dijazottak:
        if nev.upper() in d.teljesnev.upper(): # ha a kersett részlet benne a van a teljes névben
            print(f'\t{d.ev}: {d.teljesnev}({d.tipus})')

def nobeldij_statisztika():
    stat={}
    for d in dijazottak:
        if d.tipus in stat.keys():
            stat[d.tipus]+=1
        else:
            stat[d.tipus]=1
    for key, value in stat.items():
        print(f'\t{str(key).ljust(25)} {value:4d} db')

