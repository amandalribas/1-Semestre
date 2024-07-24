S, T = map(int,input().split())
possiveis = list()
for i in range (T):
    xy = list(map(int,input().split()))
    possiveis.append(xy)
total = 0
P = int(input()) #No. de sugestoes
for i in range (P):
    c = 0
    contador = 0
    atual = list(map(int,input().split()))
    for j in range (len(atual)-1):
        contador += 1
        dupla = [atual[j], atual[j+1]]
        dupla2 = [atual[j+1], atual[j]]
        if dupla in (possiveis) or dupla2 in possiveis:
            c += 1
    if c == contador-1:
        total += 1
if total == 1:
    print(1)
else:
    print(total-1)
