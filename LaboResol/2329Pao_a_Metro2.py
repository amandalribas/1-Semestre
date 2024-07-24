def fatia(x):
    total = 0
    for i in pao:
        total += i // x
    if total >= N: return True
    else: return False


N = int(input())
K = int(input())
pao = list(map(int,input().split()))
inicio = 0
fim = (sum(pao) // N) + 1
meio = (inicio + fim) // 2

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
        meio = (inicio+fim)//2
