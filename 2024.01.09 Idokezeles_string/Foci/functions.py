



def vilagbajnokok():
    darab=0
    for f in fifa:
        #Világbajnok
        if 'Világbajnok' in f.legjobb_eredmeny:
            darab+=1
    return darab        