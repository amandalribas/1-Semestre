def funcao1(): #lê informacoes do teclado
    n = int(input('Quantidade de alunos a informados: '))
    alunos = []
    for i in range (n):
        aluno = {}
        aluno['nome'] = input('Nome do Aluno(a): ')
        aluno['matricula'] = int(input(f'Matrícula de {aluno['nome']}: '))
        aluno['P1'] = float(input(f'Nota da P1 de {aluno['nome']}: '))
        aluno['P2'] = float(input(f'Nota de P2 de {aluno['nome']}: '))
        aluno['trab'] = float(input(f'Nota do trabalho de {aluno['nome']}: '))
        alunos.append(aluno)
    return (alunos)


def funcao2(nome_arquivo): #lê arquivo
    arq = open(f'{nome_arquivo}.csv')
    infos = []
    for e in arq.readlines():
        linha = list(e.strip().split('\t'))
        infos.append([linha[0], linha[1], linha[2], linha[3], linha[4]])
    print(f'{'Nome':<12}{'Matrícula':<12}{'P1':<12}{'P2':<12}{'Trabalho':<12}')
    for e in infos:
        for f in e:
            print(f'{f:<12}',end='')
        print()
    arq.close()

def media(n1,n2,t):
    return ((n1*4)+(n2*4)+(t*2))/10


def funcao3(nome_arquivo): #ordem alfabetica
    arq = open(f'{nome_arquivo}.csv')
    nomes = []
    for e in arq.readlines():
        linha = list(e.strip().split())
        nomes.append(linha[0])
    arq.close()
    nomes.sort()
    c = 0
    totais = [] #vai guardar os que já foi pra não repetir 
    print(f'{'Nome':<12}{'Matrícula':<12}{'P1':<12}{'P2':<12}{'Trabalho':<12}{'Media':<12}')
    while c != len(nomes):
        arq = open(f'{nome_arquivo}.csv')
        for e in arq.readlines():
            linha = list(e.strip().split())
            linha.append(media(float(linha[2]),float(linha[3]),float(linha[4])))
            if c < len(nomes) and linha[0] == nomes[c] and linha[0] not in totais and linha[0]:
                c = c + 1
                for f in linha:
                    print(f'{f:<12}',end='')
                print()
                totais.append(linha)
    arq.close()

def funcao4(nome_arquivo): #decrescente de media
    arq = open(f'{nome_arquivo}.csv')
    medias = []
    for e in arq.readlines():
        linha = list(e.strip().split())
        medias.append(media(float(linha[2]),float(linha[3]),float(linha[4])))
    arq.close()
    medias.sort(reverse=True)
    c = 0
    totais = [] #vai guardar os que já foi pra não repetir 
    print(f'{'Nome':<12}{'Matrícula':<12}{'P1':<12}{'P2':<12}{'Trabalho':<12}{'Media':<12}') 
    while c != len(medias):
        arq = open(f'{nome_arquivo}.csv')
        for e in arq.readlines():
            linha = list(e.strip().split())
            linha.append(media(float(linha[2]),float(linha[3]),float(linha[4])))
            if c < len(medias) and linha[5] == medias[c] and linha[5] not in totais and linha[0]:
                c = c + 1
                for f in linha:
                    print(f'{f:<12}',end='')
                print()
                totais.append(linha[5])
    arq.close()