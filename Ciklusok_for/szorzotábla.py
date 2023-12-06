#Írjuk ki a 10*10-es szorzótábla

for i in range(1,11): #i=1, i=2..i=10
    for j in range(1,11):
        print(f'{i*j:3d}',end=' ') #,3d 3 helyiértéken írjuk ki mindent
    print()    