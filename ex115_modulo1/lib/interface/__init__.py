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


def linha(tam = 42):
    res = print('-' * tam)
    return res

def cabeçalho(txt):
    linha()
    print(txt.center(42))
    linha()

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    linha()
    opc = leiaint('Sua opção: ')
    return opc
