N = int(input())
ordem =[4, 5, 6, 7, 12, 11, 13, 1, 2, 3]
t1 = t2 = 0
for i in range (N):
    atual = list(map(int,input().split()))
    j1 = j2 = 0
    for i in range (3):
        if ordem.index(atual[i]) >= ordem.index(atual[5-i]):
            j1 += 1
        else:
            j2 += 1
    if j1 >= j2:
        t1 += 1
    else:
        t2 += 1
print(t1, t2)