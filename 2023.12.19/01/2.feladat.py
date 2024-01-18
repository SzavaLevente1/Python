def tokeletes_e(szam:int)->bool:
    osszeg=0
    for oszto in range(1,szam//2+1): # // egész osztás 7//2-> 3.5-->3 (benfoglalás)
        if szam%oszto==0:
            osszeg+=oszto
    if szam==osszeg:
        return True
    return False

print('2.feladat: Tökéletes számok\nKérek két természetes számot:')
tol=int(input('tól = '))        
ig=int(input('ig = '))
print(f'Tökéletes szám {tol} és {ig} között:')        

db=0
for szam in range(tol,ig+1):
    if tokeletes_e(szam):
        if db>0:
            print('; ',end='')
        print(szam,end='')
        db+=1
if db==0:
    print('A megadott tartományon nincs tökéletes szám!')            
            