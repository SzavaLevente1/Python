gyumolcsok=['alma','banán','cseresznye','körte', 'kiwi','dinnye','mangó']
print(gyumolcsok)
# lista[tol:ig] tol - inclusive, ig - exclusive

nehany_gyumolcs=gyumolcsok[1:4] # 1-es indexű elemtől a 4.-ig egy részlista, de a 4-es már nincs benne
print(nehany_gyumolcs)
nehany_gyumolcs=gyumolcsok[3:] # 3-as indexűtől a végéig az összes elem
print(nehany_gyumolcs)
nehany_gyumolcs=gyumolcsok[:4] # az elejétől a 4.-ig egy részlista, de a 4-es már nincs benne
print(nehany_gyumolcs)
nehany_gyumolcs=gyumolcsok[-3:] # az utolsó 3 elem
print(nehany_gyumolcs)