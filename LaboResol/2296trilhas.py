N = int(input()) #Número de trilhas
trilhas = []
esforco1 = []
esfsoma1 = esfsoma2 = 0
esforco2 = []
esforco = []
indmenor = 0
for i in range (N): #Recebe os valores das trilhas e poe em uma
    trilha = list(map(int, input().split()))
    trilhas.append(trilha)

for e in trilhas:
    esftrilha = []
    for i in range (1,len(e)-1):
        if e[i+1] > e[i]:
            esftrilha.append(e[i+1] - e[i])
    esforco1.append(sum(esftrilha))

for e in trilhas:
    esftrilha = []
    for i in range (len(e)-1, 1,-1):
        if e[i-1] > e[i]:
            esftrilha.append(e[i-1] - e[i])
    esforco2.append(sum(esftrilha))

for i in range (len(esforco1)):
    if esforco1[i] <= esforco2[i]:
        esforco.append(esforco1[i])
    else:
        esforco.append(esforco2[i])

for i in range (len(esforco)):
    if i == 0:
        indmenor = i
    elif esforco[i] < esforco[indmenor]:
        indmenor = i
print(indmenor+1)