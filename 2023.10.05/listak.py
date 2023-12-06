#Eddig 4 külön változó kellet
# a=123
# b=34
# c=66
# d=87

# Lista: közös név alatt, sorszámmal indexelve tárol elemeket
lista=[] # ez egy lista ami üres

szamok=[111,34,66,87]
szinek=['piros','kék','zöld','fehér']

# Lista elemeinek elérése:
print(szamok) # teljes lista kiírása (pl. tesztelési cél)
print(*szinek,sep=' - ') #szinek lista összes eleme
# a lista elemeit 0-tól kezdődőben indexeljük
# első elem indexe 0, az utolsó elem indexe n-1
print(szamok[0]) #lista első elemének kiírása
print(szamok[-1]) #lista utolsó elemének kiírása ("kőrbefordul")

# A lista elemszáma
print(f'{len(szamok)} elem van a listában.')
print(f'A lista utolsó eleme: {szamok[len(szamok)-1]}')

# A lista bejársa, ha szükség van az indexre is
for i in range(0,len(szamok)):# 4 elemű lista esetén az indexek: 0,1,2,3 a range miatt az i értéke is 0,1,2,3
    print(f'A lista {i+1}. eleme: {szamok[i]}')

# A lista bejársa, ha nincs szükség az indexre csak az elemekre
for szam in szamok: # végigmegy a lista elemein egyesével. mindenképpen az elejétől a végéig!
    print(szam, end=' ') # szam az éppen aktuális eleme a szamok listának (bárminek nehezhetnénk)

db=0 # 3-mal oszhatók száma
for szam in szamok:
    if szam%3==0:
      db+=1
print(f'\n\n{db} db 3-mal osztató szám van a "szamok" listában.')                                