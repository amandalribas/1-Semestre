N = int(input()) #numero de estudantes na caravana
alunos = []
for i in range (N):
    alunos.append(int(input()))
media = sum(alunos)//N
for i in range (N):
    print(media-alunos[i])
    