N = int(input())
contador = 0
while N != 0:
    contador += 1 
    dados = []
    x = []
    y = []
    u = []
    v = []
    for i in range (N):
        dados = list(map(int,input().split()))
        x.append(dados[0])
        y.append(dados[1])
        u.append(dados[2])
        v.append(dados[3])
    print('Teste', contador)
    x, y, u, v = max(x), min(y), min(u), max(v)
    if u > x and y > v:
        print(f'{x} {y} {u} {v}')
    else:
        print('nenhum')
    print()
    N = int(input())