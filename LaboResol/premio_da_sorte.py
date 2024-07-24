N = int(input())
num = list(map(int,input().split()))
atual = num[0]
c = 1
possiveis = []
for i in range (1,N):
    if atual == num[i]:
        c += 1
    else:
        possiveis.append(c)
        atual = num[i]
        c = 1
possiveis.append(c)
print(max(possiveis))