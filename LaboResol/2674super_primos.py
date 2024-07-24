def primo(n):
    if n == 2:
        return 'Super'
    if (n % 2 == 0) or n == 1 or n == 0:
        return 'Nada'
    for i in range (3,int(n**(1/2))+2):
        if n % i == 0:
            return 'Nada'
    return 'Super'


def super(n):
    c = primo = 0
    while n >= 10:
        n = n//10
        c += 1
        if n == 2 or n == 3 or n == 5 or n == 7:
            primo += 1
    if c == primo:
        return 'Super'
    else:
        return 'Primo'


while True:
    try:
        N = int(input())
        if primo(N) == 'Nada':
            print(primo(N))
        else:
            print(super(N))
    
    except EOFError:
        break