#Kérjük be egy számtani sorozat első elemét (a1), differenciáját (d), és elemszámát (n)!
#Írhuk ki a sorozat ne darab elemét vesszővel elválasztva!

a1=int(input('Kerem a sorozat első elemét: '))
d=int(input('Kerem a sorozat differenciáját: '))
n=int(input('Háyn elemű legyen a sorozat?: '))

# for i in range(n): # 0..n-1--> i=0,i=1,i=2....i=n-1
#     an=a1+i*d
#     print(an, end=', ')

for i in range(n): # 0..n-1--> i=0,i=1,i=2....i=n-1
    an=a1+i*d
    if i==n-1:
        print(an, end='')# ha az utolsó jön, akkor nincs veszző
    else:
        print(an,end=', ')#amíg nem az utolsó jön, addig van vessző


    