H1, M1, H2, M2 = map(int,input().split())
while H1 != 0 or M1 !=0 or H2 != 0 or M2 != 0:
    tempo1 = tempo2 = 0
    if H1 == 0:
        tempo1 = 24 * 60
    else:
        tempo1 = H1 * 60
    if H2 == 0: 
        tempo2 = 24 * 60
    else:
        tempo2 = H2 * 60
    
    tempo1 += M1
    tempo2 += M2
    
    if tempo2 < tempo1:
        print(tempo2-tempo1 + 1440)
    else: 
        print(abs(tempo1-tempo2))    
    H1, M1, H2, M2 = map(int,input().split())
