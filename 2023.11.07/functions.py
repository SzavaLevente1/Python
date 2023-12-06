from random import randint

szamok=[]

def random_szamok(n:int,min:int,max:int)->None:
    szamok=[]
    for i in range(n):
        szamok.append(randint(min,max))
    return szamok    

def lista_kiir(szamok:list)->None:
    for i in range(len(szamok)):
        print(szamok[i],end='')
        if i<len(szamok)-1:
            print(', ',end='')        
            