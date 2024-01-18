from data import CBadás

cbAdasok:list[CBadás]=[]

def beolvas(fajlnev:str):
    f=open(fajlnev,'r',encoding='utf-8')
    f.readline()
    for sor in f:
        cbAdasok.append(CBadás(sor.strip()))
    f.close()

def bejegyzesek_szama()->int:
    return len(cbAdasok)

def nev_bejegyzesszam(nev:str)->int:
    db=0
    for adas in cbAdasok:
        if adas.nev==nev:
            db+=1
    return db
        
def maxAdasDb()->int:
    max=0
    for adas in cbAdasok:
        if adas.darab>max:
            max=adas.darab
    return max

def fajlbairas(fajlnev:str):
    f=open(fajlnev,'w',encoding='utf-8')
    f.write('Kezdes;Nev;AdasDb\n')
    for adas in cbAdasok:
        f.write(f'{adas.ora*60+adas.perc};{adas.nev};{adas.darab}\n')
    f.close()    

