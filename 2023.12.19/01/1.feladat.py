print('1.feldat A háromszög szerkezthetősége')
print('Kérem a háromszög oldalit!')
a=float(input('a = '))
b=float(input('b = '))
c=float(input('c = '))

if a+b>c and a+c>b and b+c>a:
    print('A háromszög megszerkezthető!')
else:
    print('A háromszög nem szertkezthető a megadott adatokkal!')    