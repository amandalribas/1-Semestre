def notas(arquivo1,arquivo2,arquivo3):
    total = []
    arq = open(arquivo1)
    arq2 = open(arquivo2)
    arq3 = open(arquivo3,'w')
    while True:
        nome = arq.readline().strip()
        notas = list(arq2.readline().split())
        media = 0
        if nome == '':
            break
        for e in notas:
            media = media + int(e)
        media = media / int(len(notas))
        arq3.write(f'Nome: {nome} | Média: {media:.2f} \n')

    arq.close()
    arq2.close()
    arq3.close()


arq1 = input()
arq2 = input()
arq3 = input()
notas(arq1,arq2,arq3)