produtos = (str(input('Insira o nome do produto: ')),
            int(input('Insira o valor do produto: R$')),
            str(input('Insira o nome do produto: ')),
            int(input('Insira o valor do produto: R$')),
            str(input('Insira o nome do produto: ')),
            int(input('Insira o valor do produto: R$')))

# print(f'{produtos[0]}...........................R${produtos[1]}')
# print(f'{produtos[2]}...........................R${produtos[3]}')
# print(f'{produtos[4]}...........................R${produtos[5]}')

print('-'* 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'* 40)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end = '')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('-'* 40)
