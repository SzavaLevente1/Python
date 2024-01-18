from datetime import datetime

class valtozas:
    def __init__(self,sor:str) -> None:
        adataok=sor.split(';')
        self.datum=datetime.strptime(adatpok[0],'%Y.%m.%d')
        self.benzin=int(adataok[1])
        self.gazolaj=int(adataok[2])
        
