N, T = map(int, input().split()) #N = Numero de Jogadores, T = Turnos
jogadas = list(map(int,input().split())) #Recebe os valores 
total = [] #Criação de Matriz
max = 0 #Indice do Numero Maior
for i in range (N): 
    jogador = []
    for j in range (i,N*T,N):
        jogador.append(jogadas[j])
    total.append(jogador) #Matriz com cada elemento representando um jogador

for i in range (len(total)):
    if sum(total[i]) >= sum(total[max]):
        max = i
print(max+1)
