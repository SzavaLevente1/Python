szotar={'alma':'apple','szek':'chair','ajtó':'door','kék':'blue'}
#key-value párok alkotják
print(szotar) #teljes szótár kiírása
print(szotar['kék']) # a key alapján írjuk ki a value-ban lévő értéket

for szo in szotar.keys(): # végigmegyünk a szótáron és kiirjuk a key mezők értékét
    print(szo)

for szo in szotar.values(): # végigmegyünk a szótáron és kiirjuk a value mezők értéétt
    print(szo)

for szo in szotar.items(): # végigmegyünk a szótáron és kiirjuk a key - value párokat
    print(szo)
    
#új elem hozzáadaása a szótárhoz
szotar['piros']='red' # dictoinary_neve[key_csmező]='value_mező'

# meglévő elem felülírása
szotar['kék']='navy'
print(szotar)

# dictionary bejerása úgy, hogy key-value párokat kapjunk
for key, value in szotar.items():
       print(f'{key} - {value}')
 
# Hiba: ha olyan kulcsra hivatkozunk, ami nincs a szótárban       
# print(szotar['barna'])

# kersés a dict kulcsai között 
kersett_szo=input('Keresett szó: ')    
if kersett_szo in szotar.keys():
    print(f'{kersett_szo} - {szotar[kersett_szo]}')
else:
    print(f'A {kersett_szo} mincs benne a szótárban!')
    if input('Szeretné belerakni? (i/n): ')=='i': # ha a válasz 'i' akkor 
        jelentes=input('Jelentés: ')
        szotar[kersett_szo]=jelentes

print(szotar)
    