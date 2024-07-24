P = int(input())
D = int(input())
B = int(input())
total = P + (D*2) + (B*3)
if total >= 150:
    print('B')
elif total < 150 and total >= 120:
    print('D')
elif total >= 100 and total < 120:
    print('P')
else:
    print('N')