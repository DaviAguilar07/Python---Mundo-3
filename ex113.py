def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'Erro! Digite um valor válido.')
            continue
        except (KeyboardInterrupt):
            print(f'O usuário não inseriu valor.')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'Erro! Digite um valor válido.')
            continue
        except (KeyboardInterrupt):
            print(f'O usuário não inseriu valor.')
            return 0
        else:
            return n


n1 = leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digite um número real: ')
print(f'O número inteiro digitado foi: {n1}')
print(f'O número real digitado foi: {n2}')

