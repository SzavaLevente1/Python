fajl=open('gyumolcsok.txt','r',encoding='UTF8')
#gyumolcsok.txt -fájl amit szeretnénk beolvasni
# 'r' - megnyitás módja - r: olvasásra
# encoding='UTF8' - karakterkódolás
egysor=fajl.readline() #beolvas 1 sort a fájlból és a fájl mutató a következő sorra állítja
egysor=egysor.strip() # levágja sor végéről a soremelés karaktert (ENTER-t) 
print(egysor)

kovtkezosor=fajl.readline().strip() #itt egyszerre beolvassuk és levágjuk a végéről a soremelés karaktert
print(kovtkezosor)
fajl.close # a megnyitzott fájl bezárása (nagyon fontos)

print('--------------------------------')
#Teljes fájl beolvasása
gyumolcsok=[]
fajl=open('gyumolcsok.txt','r',encoding='UTF8')

for sor in fajl:
    gyumolcsok.append(sor.strip())
fajl.close()

print(gyumolcsok)    

print('--------------------------------------')
gyumolcsok.clear() #kiürítjük a listát, hogy a következő feladatrészre üles legyen
#Ha fejléc is van a fájlban
fajl=open('gyumolcsok_fejleccel.txt','r',encoding='UTF8')
#elso_sor=fajl.readline()# HA kséőbb szükség van az első sorra
fajl.readline() # HA nincs rá szükség késöbb!!!
for sor in fajl:
    gyumolcsok.append(sor.strip())
fajl.close()
print(gyumolcsok)
