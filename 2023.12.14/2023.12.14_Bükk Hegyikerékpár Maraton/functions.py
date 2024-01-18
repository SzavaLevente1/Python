from versenytav import Versenytav
import math

versenytavok:list[Versenytav]=[]

def beolvas(fajlnev:str):
    f=open(fajlnev,'r',encoding='utf-8')
    f.readline()
    for sor in f:
        versenytavok.append(Versenytav(sor.strip()))
    f.close()
    
def celba_nem_erkezok_aranya()->float:
    return (1-len(versenytavok)/691)*100

def versenyzokszama(tav:str,nem:str)->int:
    db=0
    for v in versenytavok:
        if v.Tav()==tav and v.Nem()==nem:
            db+=1
    return db
        
def volt_tobb_mint(masodpercek):
    for v in versenytavok:
        if v.masodpercek>masodpercek:
                return True
    return False

def gyoztes(tav:str,kategoria:str)->Versenytav:
    min=math.inf
    gyoztesversenyzo=None
    for v in versenytavok:
        if v.Tav()==tav and v.kategoria==kategoria and v.masodpercek<min:
            min=v.masodpercek
            gyoztesversenyzo=v
    return gyoztesversenyzo 

def statisztika():
    stat={}
    for v in versenytavok:
        if v.Nem()=='Férfi' 
           if.kategoria in stat.keys(): 
           
           else:    
        
       
        
        