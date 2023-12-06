from datetime import datetime

class tanulo:
    def __init__(self,vezeteknev:str,keresztnev:str,szuletes:datetime,jegyek:list[int]) -> None:
        self.vezeteknev=vezeteknev
        self.keresztnev=keresztnev
        self.szuletes=szuletes
        self.jegyek=jegyek

    def atlag(self) ->float:
        if len(self.jegyek)==0: # ha nincs jegye, akkor elkerüljük a zéróosztó problémát
            return 0  # visszatérési érték a 0 lesz
        osszeg=0
        for jegy in self.jegyek:
            osszeg+=jegy
        return osszeg/len(self.jegyek)         