#Írjukn programot, amely bekéri két pont koordinátáit,
# majd kiszámolja azok távolságát
#P1(5,-3) - P1(x1,y1)
#P1(-4,-5) - P2(x2,y2)

from math import sqrt

x1=int(input('Az első pont x koordinátája: '))
y1=int(input('Az első pont y koordinátája: '))
x2=int(input('Az második pont x koordinátája: '))
y2=int(input('Az második pont x koordinátája: '))

tavolsag=sqrt((x2-x1)**2+(y2-y1)**2)
print(f'A két pont távolsága: {tavolsag}')