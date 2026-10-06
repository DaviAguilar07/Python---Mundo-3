def contador(i, f, p):
    # Docstring:
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('Fim')

contador(0, 10, 2)
# Função help, para mostrar as funcionalidades da função questionada
# help(contador)
