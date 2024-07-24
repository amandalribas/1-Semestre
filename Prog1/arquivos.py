arq = open('fodase.txt', 'w')
R = 'S'
while R not in 'Nn':
    arq.write(input('digite: '))
    arq.write('\n')
    R = input('Deseja Continuar?')
arq.close()
