lista = list(map(int,input().split())) #recebe os valores de uma lista
A = [0] * len(lista)
A[0] = lista[0]
for i in range (1, len(lista)):
    A[i] = A[i-1] + lista[i]
print(A)