a,b,c,d = map(int,input().split())
up = down = 0
listab = []
listad = []
if b == d:
    down = d
    up = a + c
else:
    for i in range (2,b+1):
        if b % i == 0:
            listab.append(i)
    for i in range (2,d+1):
        if d % i == 0:
            listad.append(i)
    if b in listad:
        down = d
        up = int(c + (a*d//b))
    elif d in listab:
        down = b
        up = int(a + (c* (b/d)))
    else:
        down = b * d
        up = int((a * d) + (c* b))
divup = []
divdown = []
for i in range (2,up+1):
    if up % i == 0:
        divup.append(i)
for j in range (2,down+1):
    if down % j == 0:
        divdown.append(j)
if up in divdown:
    up = 1
    down = down/up
elif down in divup:
    up = up/down
    down = 1
else:
    for e in divup:
        for k in divdown:
            if e == k:
                up = up // e
                down = down//e
                if e > max(divdown) or k > max(divup):
                    break
print(divup)
print(divdown)

print(f'{up:.0f} {down:.0f}')