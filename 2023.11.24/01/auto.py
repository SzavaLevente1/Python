'''
class auto: #osztály
    tipus='' # jellemzők, attribútumok
    rendszam=''
    szin=''
    teljesitmeny=''
'''

class auto:
    def __init__(self, tipus:str,rendszam:str,szin:str,teljesitmeny:float,gyorsulas:float=0) -> None: #konstruktor megadása (speciális fgv.)
        # metódus (az osztály saját függvényei)
        # a példányosításkor fut le
        # self - hivatkozás a saját osztályra, minden metódusnak első paramétere ez kell, hogy legyen
        # gyorsulas alapértelmezett értéke a 0
        self.tipus=tipus
        self.rendszam=rendszam
        self.szin=szin
        self.teljesitmeny=teljesitmeny
        self.gyorsulas=gyorsulas
        
           