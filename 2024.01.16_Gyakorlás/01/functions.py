from data import kosar

liga:list[kosar]=[]

def beolvas(fajlnev):
    f=open(fajlnev,'r',encoding='utf-8')
    f.readline
    for sor in f:
        liga.append(kosar(sor.strip()))
    f.close
    
def madrid():      
    hazai=0  
    for i in liga:
        if i.hazai==hazai:
         hazai+=1
    return hazai          
        
        
        
               