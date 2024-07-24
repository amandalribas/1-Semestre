import random

nomes = ['Alice', 'Amanda', 'Ana', 'Beatriz', 'Clara',
         'Davi', 'Emanuel', 'Joao', 'Gabriel', 'Gabriela',
         'Juliano', 'Alberto', 'Veronica', 'Pedro', 'Helena',
         'Mariana', 'Marcos', 'Miguel', 'Zivaldo', 'Lais']
sobrenomes = ['Silva', 'Leal', 'Santos', 'Machado', 'Lemos',
              'Ribas', 'Alves', 'Almeida', 'Barbosa', 'Alexandre',
              'Leite', 'Castro', 'Dias', 'Freitas', 'Garcia',
              'Lima', 'Lopes', 'Nunes', 'Pereira', 'Reis']

N = int(input('Quantos Nomes? '))
arq = open('xyz.txt', 'w')
for i in range (N):
    arq.write(f'Nome: {nomes[random.randint(0,19)]} {sobrenomes[random.randint(0,19)]} |Altura: {(1+random.random()):.2f} \n')
arq.close()
