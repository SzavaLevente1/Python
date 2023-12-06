#Bekérünk egy számot, és írjuk ki a faktoriálisát
# n!=1*2*3*4*...*(n-1)*n
# 5!=1*2*3*4*5=120

n=int(input('n= '))
faktorialis=1 #kezdőérték
print(f'{n}! =1',end='')

for i in range(2,n+1): #ha n-ig szereténk menni, a range-be n+1 kell!
    # faktorialis=faktorialis*i
    faktorialis*=i
    print(f'*{i}',end='')

print(f'={faktorialis}')


