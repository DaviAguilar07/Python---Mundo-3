def aumentar(num = 0, param = False):

    if param == True:
        aumentar = num + (num * 10 / 100)
        return f'{'R$'}{aumentar:.2f}'.replace('.', ',')

    return num + (num * 10 / 100)


def diminuir(num = 0, param = False):

    if param == True:
        diminuir = num - (num * 13/100)
        return f'{'R$'}{diminuir:.2f}'.replace('.', ',')

    return num - (num * 13 / 100)


def dobro(num = 0, param = False):

    if param == True:
        dobro = num * 2
        return f'{'R$'}{dobro:.2f}'.replace('.', ',')
    
    return num * 2


def metade(num = 0, param = False):

    if param == True:
        metade = num / 2
        return f'{'R$'}{metade:.2f}'.replace('.', ',')
    
    return num / 2


def moeda(num = 0):
    return f'{'R$'}{num:.2f}'.replace('.', ',')
