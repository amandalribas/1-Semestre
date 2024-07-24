N,M = map(int, input().split())
X = list()
ma = soma = 0
for i in range (N):
    x = list(map(int, input().split()))
    X.append(x)
    soma = sum(x)
    if soma > ma:
        ma = soma
    soma = 0
for m in range (M):
    soma = 0
    for n in range (N):
        soma += X[n][m]
    if soma > ma:
        ma = soma
print(ma)