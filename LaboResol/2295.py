A, G, RA, RG = map(float, input().split())
if (RA/A) > (RG/G):
    print('A')
elif (RG/G) > (RA/A):
    print('G')
else:
    print('G')
    