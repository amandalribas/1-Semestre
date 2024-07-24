V = int(input())
n = 0
while V != 0:
    n += 1
    print(f'Teste {n}')
    B50 = V // 50
    V = V % 50
    B10 = V // 10
    V = V % 10
    B5 = V // 5
    V = V % 5
    B1 = V // 1
    print(f'{B50} {B10} {B5} {B1}')
    print()
    V = int(input())