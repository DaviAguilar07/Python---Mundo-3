def fatorial(n, show):
    f = 1
    if show == True:
        for i in range(n, 0, -1):
            print(f'{i}', end=' x ' if i > 1 else ' = ')
            f *= i
        print(f'{f}')
    else:
        for i in range(n, 0, -1):
            f *= i
        print(f'{f}')



num = int(input('Informe um número para saber seu fatorial: '))
fatorial(num, show=True)