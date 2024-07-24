L, C, M, N = map(int,input().split())
Matriz = []
maior = 0 
for i in range (L): #Matriz Inicial
    Matriz.append(list(map(int,input().split())))

for m in range (0,L,M):
    for n in range (0,C,N):
        soma = 0
        for i in range (M):
            for j in range (N):
                soma += Matriz[m+i][n+j]
        if soma >= maior:
            maior = soma
print(maior)