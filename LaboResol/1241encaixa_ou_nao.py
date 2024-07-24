N = int(input())
for i in range (N):
    n1,n2 = map(str,input().split())
    if len(n2) <= len(n1):
        if n1[(len(n1)-len(n2)):] == n2:
            print('encaixa')
        else:
            print('nao encaixa')
    else:
        print('nao encaixa')
