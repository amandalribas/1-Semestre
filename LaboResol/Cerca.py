N, H = map(int,input().split()) #N = No. Hastes, H = Altura
lista = list(map(int,input().split()))
soma = 0
dif = 0
for i in range (N-1):
    dif = (H-lista[i])
    lista[i+1] += dif
    soma += (abs(dif))
print(soma)