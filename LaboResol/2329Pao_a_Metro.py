def fatia(x):
    total = 0
    for e in pao:
        total += e//x
    if total >= N:
        return True
    else:
        return False
    

N = int(input()) #Numero de Fatias
K = int(input()) #Numero de pãos
pao = list(map(int,input().split()))
inicio = 0
fim = (sum(pao)//N) + 1
meio = (inicio + fim) //2 

while True:
    if fatia(meio):
        if not fatia(meio+1):
            print(meio)
            break
        else:
            inicio = meio
            meio = (inicio + fim) // 2
    else:
        fim = meio
        meio = inicio+fim//2