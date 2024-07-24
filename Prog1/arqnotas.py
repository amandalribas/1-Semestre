def copia(arquivo1,arquivo2):
    arq = open(arquivo1, 'r')
    arq2 = open(arquivo2, 'w')
    for linha in arq.readlines():
        if linha[0] != ('/') and linha[1] != ('/'):
            arq2.write(linha)
    arq2.close()
    arq.close()


arq1 = input('Nome do Arquivo contendo nomes:')
arq2 = input('Nome do Arquivo a ser transferido: ')
copia(arq1,arq2)