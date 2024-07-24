V = int(input()) #Valor disponível
A = int(input()) #Conta do Açougue
F = int(input()) #Conta da Farmácia
P = int(input()) #Conta da Padaria
lista = [A,F,P]
contador = 0
for e in lista:
    if V >= min(lista):
        contador += 1
        V -= min(lista)
        lista.remove(min(lista))
print