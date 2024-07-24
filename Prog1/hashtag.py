def mudar(f):
    f = list(f.strip().split())
    return '#'.join(f)


frase = input()
print(mudar(frase))