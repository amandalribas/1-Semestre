r1 = list(map(int,input().split()))
r2 = list(map(int,input().split()))
if r1[2] + r1[3] < r2[0] + r2[1] or r2[2] + r2[3] < r1[0] + r1[0]:
    print('0')
else:
    print('1')