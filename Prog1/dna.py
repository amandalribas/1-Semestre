def DNA(palavra):
    base = ['A','T','C','G']
    trans = ['T','A','G','C']
    atual = list(palavra.strip())
    for i in range (len(atual)):
        atual[i] = trans[base.index(atual[i])]
    return ''.join(atual)

dna = input('Sequêcia de DNA: ')
print(DNA(dna))