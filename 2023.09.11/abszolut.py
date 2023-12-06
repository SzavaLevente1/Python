szam=float(input('Kérek esgy számot: '))

#összehasonlító operátork: < > <= >= == !=

if szam >= 0:
    print(f'A szám abszólút értéke:{szam}')
else:
    # print(f'A szám abszólút értéke:{szam*-1}')
    print(f'A szám abszólút értéke:{-szam}')
    print('Ez még benne van az else ágban')
print('Ez már nincs benne')

