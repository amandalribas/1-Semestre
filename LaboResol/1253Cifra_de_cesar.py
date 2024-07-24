N = int(input())
alfabeto = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z']
for i in range (N):
    pa = input()
    num = int(input())
    for e in (pa):
        print(alfabeto[alfabeto.index(e)-num], end='')