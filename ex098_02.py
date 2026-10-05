from time import sleep

def demonstraçao():
    print('Imprimindo os números de 1 a 10 (1 em 1):')
    for i in range(1, 11, 1):
        print(f'{i} ', end='', flush=True)
        sleep(1)
    print('Fim')

    print('-'*40)

    print('Imprimindo os números de 10 a 1 (2 em 2):')
    for i in range(10, 0, -2):
        print(f'{i} ', end='', flush=True)
        sleep(1)
    print('Fim')


def personalizado1(inicio, fim, contagem):
    # Evita contagem = 0
    if contagem == 0:
        contagem = 1

    # Se a contagem for positiva e início > fim, inverte o sinal
    if inicio > fim and contagem > 0:
        contagem = -contagem

    for i in range(inicio, fim + (1 if contagem > 0 else -1), contagem):
        print(f'{i} ', end='', flush=True)
        sleep(1)
    print('Fim')


demonstraçao() # Imprime a demonstração

print('-'*40)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
contagem = int(input('Contagem: '))

personalizado1(inicio, fim, contagem)
