
print('2. feldat: 2018-as VB csapatai:\n\t',end='')
csapatok=csapatok_2018()
for i in range(len(csapatok)):
    if i%4==0 and i!=0:
        print()
        print(f'\t{str(csapatok[i]).ljust(14)}',end='')
    else:    
        print(f'{str(csapatok[i]).ljust(14)}',end='')
    
    
    