rs = input()
vogais = []
inv = []
for i in range (len(rs)):
    if rs[i] in ('a','e','i','o','u'):
        vogais.append(rs[i])
for i in range (len(vogais)-1,-1,-1):
    inv.append(vogais[i])
if inv == vogais:
    print('S')
else:
    print('N')