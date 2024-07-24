N = int(input())
c = 0
while N != 0:
    c += 1
    possiveis = [[0]*10 for i in range (6)]
    for i in range (N):
        lista = list(map(str,input().split()))
        inte = list(map(int,lista[0:10]))
        letra = list(map(str,lista[10:16]))
        for j in range (0,6):
            if letra[j] == 'A':
                possiveis[j][inte[0]] += 1
                possiveis[j][inte[1]] += 1
            elif letra[j] == 'B':
                possiveis[j][inte[2]] += 1
                possiveis[j][inte[3]] += 1
            elif letra[j] == 'C':
                possiveis[j][inte[4]] += 1
                possiveis[j][inte[5]] += 1
            elif letra[j] == 'D':
                possiveis[j][inte[6]] += 1
                possiveis[j][inte[7]] += 1
            elif letra[j] == 'E':
                possiveis[j][inte[8]] += 1
                possiveis[j][inte[9]] += 1            
    print(f'Teste {c}')
    for k in range (6):
        indmax = 0
        for l in range (1,10):
            if possiveis[k][l] > possiveis[k][indmax]:
                indmax = l
        print(f'{indmax}', end=' ')
    print('\n')
    N = int(input())