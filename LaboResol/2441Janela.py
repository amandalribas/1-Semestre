def dif(X1,X2):
    return(X2-(X1+200))


F1, F2, F3 = map(int,input().split())
aberto = 0
if F1 > 0: #de 0 até F1
    aberto += F1 * 100
if dif(F1,F2) > 0: #de F1 até F2
    aberto += 100*dif(F1,F2)
if dif(F2,F3) > 0: #de F2 até F3
    aberto += 100*dif(F2,F3)
if (F3+200) < 600: #de F3 até 600
    aberto += 100*(400-F3)
print(aberto)