def super(x):
    for i in range (len(x)):
        if x[i] in '4689':
            return False
    x = int(x)
    for i in range (2,int((x**(1/2))+1)):
        if x % i == 0:
            return False
    return True

N = input()
while N!= '0':
    if super(N):
        print('Super')
    else:
        print('Normal')
    N = input()