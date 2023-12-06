#növekvényes ciklus - for

for i in range(10):
    # létrehoz egy i változót (ciklusváltozó)
    # ami felvesz a rrange fgv. által generált értékeket egymás után
    #range(10) --> 0,1,2,3,4,5,6,7,8,,9
    print('Valami')

for i in range(10,20): #10-19-ig vesz fel értékeket
    print(i)           #10x hajtódik végre ez is

for i in range(100,200,2): #100-198 kettesével
    print(i)

for i in range(200,180,-2): #200-182 -kettesével
    print(i)    

for i in range(2200,2180,2):
    #range üres tartományt ad --> egyszer sem fut le a ciklus mag
    #ciklusmag (a cilusban lévő utasítás(ok))
    print(i)

#KÉSÖBB: fo ciklus a listva vagy fájl elemein/sorain is végig tud menni!!

