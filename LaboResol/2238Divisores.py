A, B, C, D = map(int,input().split())
'''N = 1
lista = [A,B,C,D]
for i in range (max(lista)+1):
    if N % A == 0 and N % B != 0 and C % N == 0 and D % N != 0:
        print (N)
        break
    else:
        N += 1
if N >= (max(lista)):
    print('-1')'''
