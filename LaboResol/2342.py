N = int(input())
P, C, Q = map(str, input().split())
P = int(P)
Q = int(Q)
if C == '+' and (P + Q) <= N or C == '*' and (P*Q) <= N:
    print('OK')
else:
    print('OVERFLOW')
    