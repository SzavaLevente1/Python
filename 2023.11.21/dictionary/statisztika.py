szoveg = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis suscipit deleniti vel ipsum possimus. Rerum, necessitatibus qui quibusdam consequatur eius veniam beatae sit assumenda quos, minus fugiat amet aut. Repudiandae eveniet illum inventore similique modi esse ex ipsam ab officiis nemo, consequatur assumenda impedit numquam, accusantium corrupti iusto, amet soluta totam natus ipsa. Ea tenetur culpa dolores maxime sint est quia deleniti illo sed debitis enim officiis, sequi vero laboriosam quod reiciendis. Exercitationem perspiciatis enim, molestias rerum amet omnis officiis dolores porro. Nesciunt enim, dolore alias dolorem repudiandae magnam culpa. Quibusdam modi eius maiores sequi laborum, sit officia doloribus assumenda quas, rerum est eligendi harum fugit fuga. Dolore adipisci eaque labore consequuntur dicta! Ad sunt quisquam accusantium, ipsa iste, quia nihil error nesciunt nobis doloribus dicta sit ut temporibus impedit fugit consectetur. Deleniti consequuntur ex quibusdam beatae, omnis veritatis minus tenetur deserunt recusandae fugiat obcaecati. Ipsum ea, officia facilis sit, cumque veritatis magni, qui repellendus praesentium excepturi iste ab. Minus laborum vitae hic cumque numquam perferendis excepturi, molestiae quasi porro, impedit perspiciatis doloribus. Modi, iste ab necessitatibus aliquam id voluptatibus atque nihil? Dolore tempora culpa corrupti officia, praesentium adipisci illum sunt exercitationem, quo reiciendis dicta neque molestiae assumenda harum dolores?'

szavak=szoveg.split(' ') # a szöveget szétdaraboljuk a szóköz mentén, és beletesszük a szavak listába

# print(szavak)

#melyik szó hányszor szerepel a szövegben?
stat={}
for szo in szavak: # végigmegyünk a szaval listán
    if szo not in stat.keys(): # ha még eddig nem voltbenne az adott szó a kulcsmezők között
        stat[szo]=1 # akkor létrehozzuk az új dict elemet
    else: # ha már benne van
        stat[szo]+=1  # akkor a vale értéket növeljük 1-el

# print(stat)

# Melyik szavak dordulnak elő 1-nél többször?
for key, value in stat.items():
    if value>1:  #ha a value nagyobb 1, csak akkor írjuk ki
        print(f'{key} - {value} db')           
       
# Melyik szó fordul elő legtöbbször?
legtobb_value=-1 #makeresés tétele
legtobb_key=''
for key, value in stat.items():
    if value>legtobb_value:
        legtobb_value=value
        legtobb_key=key
# print(f'Legtöbbször a {legtobb_key} szó fordul elő ({legtobb_value} db)') 
# az első legtöbb_value értékű szót adja csak ereményül
legtobb_value=(max(stat.values())) # a maxkeresés progtétel helyett

# lehet, hogy több maximum van:
print(f'Legtöbbször ({legtobb_value} alkalommal) előforduló szavak: ')
for key, value in stat.items():
    if value==legtobb_value:
        print(f'\t{key}')           