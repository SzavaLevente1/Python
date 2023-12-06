# 12 vesenyző
# Mnden versenyző 6-ot ugrik
# Szimuláljuk le a versenyt
# Ugársok 7 és 8.50 között legyenek, 30% esély, hogy érvénytelen 

# 1. versenyző ugrásai: 7.80 8.10 érvénytelen 7.56 érvénytelen 8.34
# 1. versenyző legjobb ugára: 8.34
# 2. versenyző...

from random import randint

def ugrasok_generalasa()->list:
    ugrasok=[]
    for i in range(6):
        egy_ugras=randint(700,850)/100
        if randint(1,10)<=3: # 30% esély
            egy_ugras=0
        ugrasok.append(egy_ugras)
    return ugrasok

def print_egy_versenyzo(rajtszam:int,ugrasok:list) ->None:
    print(f'{rajtszam}. versenyző ugrásai:',end=' ')
    for ugras in ugrasok:
        if ugras==0:
            print('érvénytelen', end=' ')
        else:    
            print(ugras,end=' ')
    print(f'\n{rajtszam} versenyző legjobb ugrása: {versenyzo_legnagyobb_ugrasa(ugrasok)}') #legjobb ugrás kiírása

def versenyzo_legnagyobb_ugrasa(ugrasok:list) ->float:
    legnagyobb=ugrasok[0]
    for ugras in ugrasok[1:]:
        if ugras>legnagyobb:
            legnagyobb=ugras
    return legnagyobb 

def gyoztes(erdemenyek:list) ->int:
    """
    Megkeresi és visszaadja a győztes versenyző rajtszámát .
    """
    legjobb=0
    for i in range(len(erdemenyek)):
        if erdemenyek[i]>erdemenyek[legjobb]:
            legjobb=i
    return legjobb+1 

def ervenytelen_ugrasok_szama(ugrasok:list) ->int:
    darab=0
    for ugras in ugrasok:
        if ugras==0:
            darab+=1
    return darab                      