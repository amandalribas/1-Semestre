n = int(input()) #numero de termos 
N = list(map(int,input().split())) #lista inicial
pa = int(((1+n)*n)//2) #Progressao aritmetica de n termos e de razao 1
aux = [0]*n 
soma = 0
pt = ((sum(N)//n)+1) - n//2 #primeiro termo
if sum(N) < pa:
    print('-1')
elif n % 2 == 1: #se for impar
    if sum(N) % n != 0:
        print('-1')
    else:
        for i in range (n):
            aux[i] = (sum(N)//n) + i - 2
            soma += abs(N[i] - aux[i])
        print(f'{soma//2:.0f}')
elif n % 2 == 0: #se for par
    if (sum(N)-pa) % n == 0:
        for i in range (n//2):
            aux[i] = pt + i
            soma += abs(N[i]-aux[i])
        print(f'{soma//2}')
    else:
        print('-1')    

