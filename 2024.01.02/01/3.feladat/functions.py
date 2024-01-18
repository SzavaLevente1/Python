from data import Fogadasi_fordulo

fordulok:list[Fogadasi_fordulo]=[]

def beolvas(fajlnev:str):
    f=open(fajlnev,'r',encoding='utf-8')
    f.readline()
    for sor in f:
        fordulok.append(Fogadasi_fordulo(sor.strip()))
    f.close()
        
def fordulok_szama()->int:
    return len(fordulok) 

def telitalatok_szama()->int:
    db=0
    for fordulo in fordulok:
        db+=fordulo.t13p1
    return db

def dontetlen_mentes()->bool:
    for fordulo in fordulok:
        if 'X' not in fordulo.eredmenyek:
            return True
    return False               