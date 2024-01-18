from data import Eredmény

eredmenyek:list[Eredmény]=[]

def beolvasas(fajlnev:str):
    f=open(fajlnev,'r',encoding='utf-8')
    f.readline()
    for sor in f:
        eredmenyek.append(Eredmény(sor.strip()))
    f.close()
    
def versenyzoszam()->int:
    return len(eredmenyek)

def noi_teljes()->int:
    db=0
    for e in eredmenyek:
        if e.kategoria=='Noi' and e.teljesitett==100:
            db+=1
    return db

def leghosszabb_nev()->Eredmény:
    max_hossz=eredmenyek[0]
    for e in eredmenyek:
        if len(e.nev)>len(max_hossz.nev):
            max_hossz=e
    return max_hossz                

def atlag()->float:
    db=0
    osszeg=0
    for e in eredmenyek:
        if e.kategoria=='Ferfi' and e.teljesitett==100:
            db+=1
            ido_darabok=e.ido.split(':')
            osszeg+=int(ido_darabok[0])*3600+int(ido_darabok[1])*60+int(ido_darabok[2])
    return (osszeg/3600)/db              
        