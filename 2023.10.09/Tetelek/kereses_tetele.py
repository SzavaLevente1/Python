# Mondjuk meg hogy egy elem benne van-e a listában, és ha igen, akkor hányadik?

from random import randint
szamok=[]
for i in range(100):
    szamok.append(randint(-100,100))
print(szamok)    

keresett=int(input('Kersett szám: '))

# V1
# Univerzális megoldás
index=0
while index<len(szamok) and szamok[index] !=keresett:
    index+=1
if index==len(szamok):
    print('A keresett szám nincs benne a listában')
else:
    print(f'A keresett szám a {index+1} a listában')
#Az első megtalált elem indexét ajda vissza, utána kilép a ciklusból.
 

# V2:
# Python specifikus megoldás
for i in range(len(szamok)):
    if szamok[i]==keresett:
         print(f'A keresett szám a {i+1} a listában')
         break
else:
    print('A keresett szám nincs benne a listában')

