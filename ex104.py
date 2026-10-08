def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro! Tente novamente.')
        if ok:
            break
    return valor

n = leiaint(f'Digite um número: ')
print(f'O número informado foi {n}')
