a,b,c,d = map(int,input().split())
div1, div2 = b, d
up = 0
down = 1
divb = []
divd = []
mmc = []
for i in range (2,b+1):
    if b % i == 0:
        divb.append(i)
        b = b / i 
for i in range (2, d+1):
    if d % i == 0:
        divd.append(i)
        d = d / i

if divd > divb:
    maior = divb
    menor = divb
else:
    maior = divb
    menor = divb

for e in maior:
    if e in menor:
        menor.remove(e)

mmc = maior + menor
for e in mmc:
    down *= e
up = int((a * (down/div1)) + (c *(down/div2)))
cima, baixo = up, down

divdown = []
divup = []
for i in range (2,down+1):
    if down % i == 0:
        divdown.append(i)
        down = down/i
for i in range (2,up+1):
    if up % i == 0:
        divup.append(i)
        up = up/i
if divup > divdown:
    maior = divup
    menor = divdown
for e in maior:
    if e in menor:
        baixo = baixo / e
        cima = cima / e

print(f'{cima:.0f} {baixo:.0f}')