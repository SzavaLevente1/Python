from math import sqrt

szam=int(input('Írj be egy pozitív egész számot: '))

for i in range(2,int(sqrt(szam))+1):
    if szam%i==0:  # találtunk egy osztót
        print('Nem prím!') # találtunk osztót
        break  # amint megállpítottuk, hogy prím, kiugrunk a ciklusból
else: # akkor fut le, ha a for ciklusban nem volt break!
    print('Prím!')
