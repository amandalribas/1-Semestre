c = 1
P, R = map(int,input().split()) #Partidas e Rodadas
while P != 0 and R != 0:
    ordem = list(map(int,input().split()))
    vivos = ordem[:]
    for i in range (R): 
        partida = list(map(int,input().split()))
        acao = partida[1]
        partida.pop(0)
        partida.pop(0)
        rem = 0
        for i in range (len(partida)):
            if partida[i] != acao:
                   vivos.pop(i-rem)
                   rem += 1
    print(f'Teste {c}')
    print(vivos[0])
    print()
    c += 1
    P, R = map(int,input().split())