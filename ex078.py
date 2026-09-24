numeros = []
maior = 0
menor = 0
for n in range(0,5):
    numeros.append(int(input(f'Insira um valor: ')))
    if n == 0:
        maior = menor = numeros[n]
    else:
        if numeros[n] > maior:
            maior = numeros[n]
        if numeros[n] < menor:
            menor = numeros[n]

print(f'A sequência de valores é {numeros}.')
print(f'O maior valor é {maior} nas posições ',end = '')
for indice, valor in enumerate(numeros):
    if valor == maior:
        print(f'{indice}... ',end = '')

print(f'\nO menor valor é {menor} nas posições ', end = '')
for indice, valor in enumerate(numeros):
    if valor == menor:
        print(f'{indice}... ',end = '')
        print('\n')
        