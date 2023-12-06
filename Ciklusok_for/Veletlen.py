import random #véletlen szám generálásához szükséges

for i in range(20): #20-szor fut le
    print(random.randint(1,10)) #1-10 között generál(1,10 is lehet) egész számot


x=random.random() #valós szám? DE 0<=x<1
print(x)


a=random.randrange(0,101,2) #random páros szám 0-100 között
print(a)                    #mint a range esetében a felső határ nincs benne a generált elemek között!!


