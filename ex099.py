from time import sleep
def maior(*num):
    qtd = len(num)
    maior = max(num)
    for i in num:
        print(f'{i} ', end = '', flush=True)
        sleep(0.4)
    print(f'Foram digitados {qtd} valores.')
    print(f'O maior valor digitado é: {maior}.')
    print()

maior(8, 5, 7, 6, 5, 4)
maior(1, 3, 4)
maior(10, 2)
