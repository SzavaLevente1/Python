zoldseg=input('Adja meg a zöldésg nevét: ')

#fajl=open('zoldsegek.txt','w',encoding='UTF8')
# 'w' - írásra nyitja meg a fájlt
#  ha nem létezik, akkor létrehozza
# ha létezik, akkor felülírja!
 
fajl=open('zoldsegek.txt','a',encoding='UTF8') 
# 'a' -append -> hozzáfűzés
#  ha nem létezik, akkor létrehozza
# ha létezik, akkor a végéhez hozzáfűzi

fajl.write(zoldseg+'\n') # 1 sor írása a fájlba

zoldsegek=['hagyma','krumpli','paprika','zeller']
#egy lista tartalmának fájlban írása (sornként)
for zoldseg in zoldsegek:
    fajl.write(zoldseg+'\n')

fajl.close() 