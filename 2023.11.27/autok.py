from auto import auto

autok:list[auto]=[]

def autok_betolt():
    fajl=open('autok.txt','r',encoding='utf8')
    for sor in fajl:
        #AA-BB-123;Opel;Astra J;75.0;Piros
        adatok=sor.strip().split(';')
        uj_auto=auto(adatok[0],adatok[1],adatok[2],float(adatok[3]),adatok[4])
        autok.append(uj_auto)
        #autok.append(auto(adatok[0],adatok[1],adatok[2],adatok[3],adatok[4]))
    fajl.close()    

def autok_kiir(autok_listaja:list[auto]):
    for a in autok_listaja:
        print(f'{a.rendszam.ljust(10)} {a.marka.ljust(10)} {a.tipus.ljust(10)} {a.szin.ljust(10)} {str(a.teljesitmeny).ljust(10)}')

def auto_beker():
    print('Kérem adja mega az új auto adatait')
    rendszam=input('Rendszám:')
    marka=input('Márka:')
    tipus=input('Típus:')
    teljesitmeny=float(input('Teljesítmény:'))
    szin=input('szín:')
    #eltároljuk a memóriában
    uj_auto=auto(rendszam,marka,tipus,teljesitmeny,szin)
    autok.append(uj_auto) # hoozáírjuk az új autót az eddigi listához(végére)

    #elmentjük fájlba
    fajl=open('autok.txt','a',encoding='utf8')
    fajl.write(rendszam+';'+marka+';'+tipus+';'+str(teljesitmeny)+';'+szin+'\n')
    fajl.close()
    
def legerosebb()->auto:
    legerosebb_auto=autok[0] #kezdetben a lista első eleme
    for a in autok[1:]:
        if a.teljesitmeny>legerosebb_auto.teljesitmeny:
            legerosebb_auto=a
    return legerosebb_auto #visszatérési érték a legerősebb autó osztálypéldány(minden adata elérhető)        

def autok_szin_alapjan(szin:str)->list[auto]:
    autok_uj_listaja=[]
    for a in autok:
        if a.szin.upper()==szin.upper():
            autok_uj_listaja.append(a)
    return autok_uj_listaja        
        
    
    
