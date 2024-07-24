N, M = map(int,input().split()) #Temperatura e Intervalos
c = 0
while N != 0 and M != 0:
    linha = []
    for i in range (N):
        linha.append(int(input()))
    acumulada = [] #lista acumulada
    soma = 0
    for j in range (N):
        acumulada.append(linha[j]+soma)
        soma = acumulada[j]
    ok = []
    ok.append(acumulada[M-1])
    for k in range (1,N-M+1):
        ok.append(acumulada[k+M-1] - acumulada[k-1])
    c += 1
    print(f'Teste {c}')
    print(f'{int((min(ok))/M)} {int((max(ok))/M)}')
    print()
    N, M = map(int,input().split())