#a: 20-40
#b: 30-80
#c: 20-60
# Mennyi a hármoszög kerület


print('Adja meg a háromszög oldalait!')

a=0
while a<20 or a>40:
    a=int(input('a (20-40)='))
b=-1
while b<0 or b>80:
    b=int(input('b (0-60)='))    
c=0
while c<20 or c>60:
    c=int(input('b (20-60)='))
print(f'Kerület = {a+b+c}')

print(f'{a}:{str(b).zfill(2)}:{c}')