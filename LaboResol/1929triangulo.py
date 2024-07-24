A, B, C, D = map(int,input().split())
resp = 'aa'
pos = [A, B, C]
c = 0 #A, B, C
while resp not in 'SN' :
    for i in range (len(pos)):
        if pos[0] + pos[1] > pos[2] and pos[0] + pos[2] > pos[1] and pos[1] + pos[2] > pos[0]:
            resp = 'S'
        else:
            if c == 0:
                pos[0] = D #B,C,D
            elif c == 1: #A, D, C
                pos[0] = A
                pos[1] = D
            elif c == 2: #A, B, D
                pos[1] = B
                pos[2] = D
            else:
                resp = 'N'
            c += 1
print(resp)