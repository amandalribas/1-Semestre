N = int(input())
for i in range (N):
    palavra = input()
    num = int(input())
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for e in (palavra):
        dif = alfabeto.index(e) - num
        print(alfabeto[dif], end='')
    print()