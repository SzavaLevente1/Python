from tavolugras import ugrasok_generalasa,print_egy_versenyzo,versenyzo_legnagyobb_ugrasa,gyoztes,ervenytelen_ugrasok_szama

eredmeynek=[] # minden versenyző legjobb ugrása
volt_legalabb_3_ervenytelen=False

for i in range(12):
    ugrasok=ugrasok_generalasa() # 1 versenyző generált ugrásai kerülnek az ugrasok listába
    print_egy_versenyzo(i+1,ugrasok)
    eredmeynek.append(versenyzo_legnagyobb_ugrasa(ugrasok))
    if ervenytelen_ugrasok_szama(ugrasok)>=3:
        volt_legalabb_3_ervenytelen=True


print(f'\nA győztes versenyző rajtszáma: {gyoztes(eredmeynek)}')

# Van-e olyan versenyző, akinek legalább 3 érvénytelen ugrása volt?
if volt_legalabb_3_ervenytelen:
    print('Van olyan versenyző, akiknek legalább 3 érvénytelen ugrása volt')
else:
    print('Nincs  olyan versenyző, akiknek legalább 3 érvénytelen ugrása volt')

