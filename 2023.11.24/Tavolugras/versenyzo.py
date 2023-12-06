class versenyzo:
    def __init__(self, nev:str,elso:float,masodik:float,harmadik:float) -> None:
        self.nev=nev
        self.elso=elso
        self.masodik=masodik
        self.harmadik=harmadik
        
    def legnagyobb_ugras(self): #tagfüggvény
        ugrasok=[]
        ugrasok.append(self.elso)
        ugrasok.append(self.masodik)
        ugrasok.append(self.harmadik)
        return max(ugrasok) # a 3 ugrás közül a legnagyobbat adja vissza
            