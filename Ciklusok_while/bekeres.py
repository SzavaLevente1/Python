# Ellenőrzött adatbekérés 10 és 100 között fogadunk el számokat

szam=-1 #olyan kezdőértéket kell, ami teljesíti a feltételt(ebben az esetben azt jelenti, hogy nekünk nem felel meg ez a kezdeti érték!!!)
while szam<10 or szam>100: #ha telejesül majd a feltétel akkor fut le a ciklus magja (ha nem jó az érték!)
    # szam=int(input('Kérek egy számot 10 és 100 között: '))
    #ez csak akkor lenne jó, ha tutira egész számot ad meg a felhasználó
    input_txt=(input('Kérek egy számot 10 és 100 között: '))
    if input_txt.isnumeric(): #csak számjegy, tizedes pont, - előjel nem
        szam=int(input_txt)
    else:
        print('Kérem pozitív egész számot adjon meg!')   


#Késöbb:
# saját fgv. float_input() --> valós szám  ellenőrzötten        
#  int_input() --> valós szám  ellenőrzötten (negatív is akár)
       