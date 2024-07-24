N = int(input())
postes = [0]*N
for i in range (N):
    postes[i] = int(input())
maior = c = 0
if postes[-1] + postes[0] < 1000:
    c += 1
for i in range (N-1):
    if postes[i]+postes[i+1] < 1000:
        c += 1
    else:
        c = 0
    if c > maior:
        maior = c
print(maior)