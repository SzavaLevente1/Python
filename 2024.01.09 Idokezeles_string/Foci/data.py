class foci:
    def __init__(self,sor:str) -> None:
        adatok=sor.split(';')
        self.csapat=adatok[1]
        self.reszvet=int(adatok[2])
        self.elso=adatok[3]
        self.utolso=adatok[4]
        self.elso=adatok[5]
        
    
    