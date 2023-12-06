#Irjuk ki a páros számokat 2 végérték között

eleje=int(input('Eleje '))
vege=int(input('Vége '))

if eleje%2!=0: #ha az intevallum kezdete nem páros
    eleje+=1 # így páros lesz

for i in range(eleje,vege,2):
    print(i,end=' ')    
