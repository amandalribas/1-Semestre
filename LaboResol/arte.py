N = int(input())
num = list(map(int,input().split()))
c = 1
soma = num[0] + num[-1]
for i in range (1,N//2):
    if num[i]+num[N-1-i] == soma:
        c += 1
if N % 2 == 1:
    if c == N//2 and num[N//2] == soma:
        print('S')
    else:
        print('N')
else:
    if c == N//2:
        print('S')
    else:
        print('N')