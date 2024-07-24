N = int(input())
produtos = []
for i in range (N):
    produtos.append(int(input()))
produtos.sort(reverse=True)
soma = sum(produtos)
for i in range (2,N,2):
    x = produtos 
    soma = soma - produtos[i]
print(soma)