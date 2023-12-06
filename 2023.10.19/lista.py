from random import randint

szamok=[]
def feltolt(n: int, min:int, max:int) -> None:
    #feltölti a listát 'n' db 'min' és 'max' közötti értékű elemmel 
    for i in range(n):
        szamok.append(randint(min,max))

def osszegzes()->int:
    # A szamok lista elemeinek összegét adja vissza.
    osszeg=0
    for szam in szamok:
        osszeg+=szam
    return osszeg


