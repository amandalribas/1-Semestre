A = [1,2,3,4,5,1]
c = 0
for e in A:
    A.remove(e)
    if e in A:
        print('true')
    else:
        print('nao')
    A.insert(c,e)
    c += 1
