N = int(input())
M = list(map(int,input().split()))

A = [0]*N
A[0] = M[0] 
for i in range (1,N): #auxiliar
    A[i] = A[i-1] + M[i]
maior = 0
for i in range (1,N):
    for j in range (i+1,N-1):
        atual = A[j] - A[i-1] + (j - i) - 1
        if atual > maior:
            maior = atual
print(maior)
