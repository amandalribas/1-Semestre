N = int(input())
for i in range (N):
    M = int(input())
    alunos = list(map(int,input().split()))
    ord = sorted(alunos, reverse=True)
    c = 0
    for j in range (M):
        if ord[j] == alunos[j]:
            c += 1
    print(c)
