from random import randint

# Lotto 5/90 5 szám 1-90 tartományon
#még nem tudunk imsétlődés nélkül generálni, majd azt késöbb megoldjuk

print('Az ötöslotto e heti nyerőszámai: ',end='')
for i in range(5):
    print(randint(1,90),end=' ')

#Lotto 6/45 6 szám 1-45

print('\nA hatoslotto e heti nyerőszámai: ',end='')
#for i in range(1,7):
#for i in range(0,6)
#for i in range(0,6,1)
for i in range(6):
    print(randint(1,45),end=' ')

    