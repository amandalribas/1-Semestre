a = 'amanda'
b = 'lemos'
c = '14/07/2005'
lista = ['banana', 'uva', 'morango']
frase = 'pipipi popopo ai que nao sei o que la'
burrao = '                top demais            '
print(a*5)
print(a+b)
print('abc' in a)
print(len('Teste'))

#'string'.count('elemento',inicio,fim)
print('fodase'.count('e'))
print(a.count('a',2))
print(b.count('o',0,-1)) #vai do 0 até -1

#'string'.index('elemento', inicio,fim), da erro se nao acha o elemento
print(b.index('e')) #primeira vez que aparece determinado termo
print(a.index('a',2,4))

#'string'.find('elemento',inicio,fim) retorna -1 se não encontrou
print(a.find('nd',0,2)) #como nao tem print -1
print(b.find('e')) 

#'string'.partition(separador), divide a string em 3,antes, separador e depois
print(c.partition('/')) #nao pode tá vazio
print(c) #nao modifica a string padrão
print(c.partition('*')) #caso o argumento não esteja na string, retorna a string padrãso e duas vazias

#'separador'.join('sequencia') #nao modifica a original
print('-'.join(a)) 
print('aaaaaa'.join(b[2:5]))
print('-'.join(lista))
print('-----'.join(('1','2','3','4')))

#'string'.split('separador') #se o argumento tiver vazio, separa por espaço
print(frase.split())
print(frase) #nao modifica a string original
print(a.split('a'))

#'string'.strip() #sem especificar tira os caracteres em branco
print(burrao.rstrip()) #tira da direita
print(burrao.lstrip()) #tira da esquerda
print(burrao.strip()) #tira começo e fim
print(burrao) #nao muda a string original
print(a.strip('a')) 
print(a.rstrip('a'))
print(a.lstrip('a'))

#'string'.replace(velha,nova,quantas_vezes) #nao modifica a original
print(frase.replace('ai', 'eu'))
print(frase.replace('pi','pu',2))