from functools import cmp_to_key #adaptador, padrão de projetos

def cmp_medalhas(pais1,pais2):
	if pais1[1] < pais2[1]:
		return 1
	elif pais1[1] > pais2[1]:
		return -1
	elif pais1[2] < pais2[2]:
		return 1
	elif pais1[2] > pais2[2]:
		return -1
	elif pais1[3] < pais2[3]:
		return 1
	elif pais1[3] > pais2[3]:
		return -1
	elif pais1[0] > pais2[0]:
		return 1
	elif pais1[0] < pais2[0]:
		return -1
	else:
		return 0 


N = int(input()) #numero de paises
total = []
for i in range (N):
    atual = (list(input().split()))
    atual = [atual[0], int(atual[1]), int(atual[2]), int(atual[3])]
    total.append(atual)
nova = sorted(total, key=cmp_to_key(cmp_medalhas))
for e in nova:
	print(f'{e[0]} {e[1]} {e[2]} {e[3]}')