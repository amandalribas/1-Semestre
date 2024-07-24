N = int(input())
M = []
for i in range (N):
    M.append(list(map(int,input().split())))
A = [0 * N for _ in range (N)]
A[0][0] = M[0][0]
for j in range (1,N): #Linha 0
    A[0][j] = A[0][i-1] + M[0][j]

for i in range (1,N):
    A[i][0] = M[i][0] + A[i-1][0] 