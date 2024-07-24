def mudanca(frase,antiga,nova):
    aux = frase.split()
    for i in range (len(aux)-1,-1,-1):
        if antiga in aux[i]:
            aux[i] = nova
            return ' '.join(aux)
        

frase = input('Frase: ')
antiga = input('Palavra Antiga: ')
nova = input('Palavra Nova: ')

print(mudanca(frase,antiga,nova))
