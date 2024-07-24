pA, cB, pB, cA = map(str,input().split())
pA, cB, pB, cA = int(pA[0:2]), int(cB[0:2]), int(pB[0:2]), int(cA[0:2])
fuso = sec = 0
fuso = ((cB - pA) - (cA - pB)) // 2
print(fuso)