def contador (p):
    p = list(p.strip().split())
    return(len(p))

frase = input()
print(contador(frase))
