import math #matematikai függvények használatáhot elengedhetetlen

a_oldal=int(input('A háromszög "a" oldala: '))
b_oldal=int(input('A háromszög "b" oldala: '))
c_oldal=int(input('A háromszög "c" oldala: '))

#Logikai opreátor: ÉS: and VAGY: or TAGADÁS: not
if ((a_oldal+b_oldal)>c_oldal) and ((b_oldal+c_oldal)>a_oldal) and ((a_oldal+c_oldal)>b_oldal):
   kerulet=a_oldal+b_oldal+c_oldal
   print(f'A háromszög kerülete: {kerulet}')

   s=kerulet/2
   terulet=math.sqrt(s*(s-a_oldal)*(s-b_oldal)*(s-c_oldal))
   
   print(f'A háromszög kerülete: {terulet:.3f}')
   print(f'A háromszög kerülete: {round (terulet,3)}')
   # print(round(3.5))
   # print(f'{2.5:.0f}')

else:
   print('A háromszög NEM meegszerkeszthető') 
