def verfic(item,dom):
    if item[1] == dom[1]:
        return ordem_dom[ordem.index(item[0])]
    else:
        return ordem_nao[ordem.index(item[0])]


ordem_dom = [14,15,16,17]
ordem_nao = [10,11,12,13]
ordem = ['A', 'J', 'Q', 'K']

inicial = input()
luana = [0]*3
edu = [0]*3
val_luana = val_edu = 0
for i in range (3): #Luana
    luana[i] = input()
    val_luana += verfic(luana[i],inicial)
for i in range (3): #Edu
    edu[i] = input()
    val_edu += verfic(edu[i],inicial)

if val_edu > val_luana:
    print('Edu')
elif val_luana > val_edu:
    print('Luana')
else:
    print('empate')