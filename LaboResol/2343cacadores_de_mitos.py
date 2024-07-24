N = int(input())
lista = list()
for i in range (N):
    lista.append(input())
conjunto = set(lista)
if len(conjunto) == len(lista):
    print('0')
else:
    print('1')