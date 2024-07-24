total = []
for i in range (5):
    linha = list(map(int,input().split()))
    total.append(linha[1:])
K = int(input())
valores = []
for i in (total[0]):
    for j in (total[1]):
        for k in (total[2]):
            for l in (total[3]):
                for m in (total[4]):
                    valores.append(i+j+k+l+m)
valores.sort(reverse=True)
print(sum(valores[:K]))