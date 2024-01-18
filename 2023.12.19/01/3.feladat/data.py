class Eredmény:
    def __init__(self,sor:str) -> None:
        adatok=sor.split(';')
        self.nev=adatok[0]
        self.rajtszam=int(adatok[1])
        self.kategoria=adatok[2]
        self.ido=adatok[3]
        self.teljesitett=int(adatok[4])


