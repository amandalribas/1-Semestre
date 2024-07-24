def funcao1(): #lê informacoes do teclado
    n = int(input('Quantidade de alunos a informados: '))
    alunos = [] #lista de dicionarios
    for i in range (n):
        aluno = {}
        aluno['nome'] = input('Nome do Aluno(a): ')
        aluno['matricula'] = int(input(f'Matrícula de {aluno['nome']}: '))
        aluno['P1'] = float(input(f'Nota da P1 de {aluno['nome']}: '))
        aluno['P2'] = float(input(f'Nota de P2 de {aluno['nome']}: '))
        aluno['trab'] = float(input(f'Nota do trabalho de {aluno['nome']}: '))
        alunos.append(aluno)
    arq_nome = input('Nome do Arquivo (não incluir .csv): ') #caso não precise salvar de imediato, desconsiderar
    funcao7(alunos, arq_nome) #caso não precise salvar de imediato, desconsiderar
    return (alunos)


'''def printar(nome_arquivo): #printa arquivo (usei pra conferir) 
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
    arq.close()'''

def funcao2(nome_arquivo1,nome_arquivo2): 
    arq = open(f'{nome_arquivo1}.csv') #abre o primeiro arquivo
    total = [] #vai armazenar em forma de matriz cada linha do arquivo
    for e in arq.readlines():
        total.append(list(e.strip().split()))
    arq.close()
    
    arq = open(f'{nome_arquivo2}.csv', 'w')
    for e in total:
        arq.write(f"{e[0]} \t {e[1]} \t {e[2]} \t {e[3]} \t {e[4]} \n")
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


def funcao5(nome_arquivo,matricula): #verifica presenca 
    arq = open(f'{nome_arquivo}.csv')
    for e in arq.readlines():
        linha = e.strip().split()
        if int(linha[1]) == int(matricula):
            return True
    else:
        return False



def funcao6(nome_arquivo,matricula,opcao, opcao2): #Edição
    arq = open(f'{nome_arquivo}.csv', 'r+')
    c = 0
    total = []
    for e in arq.readlines():
        linha = list(e.strip().split())
        if linha[1] == matricula:
            linha[opcao] = opcao2
        total.append(linha)
    arq.close()

    arq = open(f'{nome_arquivo}.csv', 'w')
    for e in total:
        arq.write(f"{e[0]} \t {e[1]} \t {e[2]} \t {e[3]} \t {e[4]} \n")
    arq.close()



def funcao7(lista,nome_arquivo): #salva informacoes
    arq = open(f'{nome_arquivo}.csv', 'w')
    for e in lista:
        arq.write(f"{e['nome']} \t {e['matricula']} \t {e['P1']} \t {e['P2']} \t {e['trab']} \n")
    print('Dados Armazenados.')
    arq.close()


def funcao8(nome_arquivo, matricula): #apaga registro
    arq = open(f'{nome_arquivo}.csv')
    total = []
    for e in arq.readlines():
        linha = list(e.strip().split())
        if int(linha[1]) != int(matricula):
            total.append(linha)
    arq.close()

    arq = open(f'{nome_arquivo}.csv', 'w')
    for e in total:
        arq.write(f"{e[0]} \t {e[1]} \t {e[2]} \t {e[3]} \t {e[4]} \n")
    arq.close()
    print(f'Registro de {matricula} apagado com sucesso!')

#programa principal
N = 1
while N != 9:
    print('''[1] LER INFORMAÇÕES DE UM ALUNO A PARTIR DO TECLADO;
[2] ESCOLHER UM ARQUIVO PARA LEITURA E INFORMACOES;
[3] LISTAR OS ALUNOS EM ORDEM ALFABETICA;
[4] LISTAR OS ALUNOS EM ORDEM DECRESCENTE DA MÉDIA;
[5] VERIFICAR SE UM ALUNO ESTÁ NO ARQUIVO;
[6] EDITAR INFORMAÇÕES DE UM ALUNO;
[7] SALVAR INFORMAÇÕES;
[8] APAGAR REGISTRO DE UM ALUNO;
[9] SAIR --''')
    N = int(input('Opção escolhida: '))
    if N == 1:
        total = funcao1()
        print()
    elif N == 2:
        arq_nome = input('Nome do Arquivo Original(não incluir .csv): ')
        arq_nome2 = input('Nome do Arquivo Novo(não incluir .csv): ')
        funcao2(arq_nome,arq_nome2)
        print()
    elif N == 3:
        arq_nome = input('Nome do Arquivo (não incluir .csv): ')
        funcao3(arq_nome)
        print()
    elif N == 4:
        arq_nome = input('Nome do Arquivo (não incluir .csv): ')
        funcao4(arq_nome)
        print()
    elif N == 5:
        arq_nome = input('Nome do Arquivo (não incluir .csv):' )
        m = int(input('Matrícula cadastrada: '))
        if funcao5(arq_nome,m):
            print(f'{m} já Cadastrado(a)!')
        else:
            print(f'{m} não foi Cadastrado(a)!')
        print()
    elif N == 6:
        arq_nome = input('Nome do Arquivo (não incluir .csv):' )
        m = input('Matrícula cadastrada: ')
        print(f'''INFORMACAO A SER TROCADA:
[0] NOME
[1] MATRICULA
[2] NOTA DA P1
[3] NOTA DA P2
[4] NOTA DO TRABALHO''')
        n = int(input('Opção escolhida:'))
        nova_opcao = eval(input('Será Substituido por:'))
        funcao6(arq_nome,m,n, nova_opcao)
        print()
    elif N == 7:
        arq_nome = input('Nome do Arquivo (não incluir .csv): ')
        funcao7(total, arq_nome)
    elif N == 8:
        arq_nome = input('Nome do Arquivo (não incluir .csv): ')
        m = int(input('Matrícula cadastrada: '))
        if funcao5(arq_nome,m):
            funcao8(arq_nome,m)
        else:
            print(f'{m} Não está no Cadastro. Tente novamente')
    else:
        print('OPÇÃO INVÁLIDA. Tente Novamente')
