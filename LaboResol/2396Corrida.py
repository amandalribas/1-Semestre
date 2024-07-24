N, M = map(int,input().split()) #N = Carros, M = Corridas
total = []
for i in range (N):
    total.append(sum(list(map(int,input().split()))))
ordenada = sorted(total)
for i in range (3):
    print(total.index(ordenada[i])+1)
