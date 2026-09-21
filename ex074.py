from random import randint

tupla = (randint(1, 10), randint(1, 10), randint(1, 10),
         randint(1, 10), randint(1, 10))

print(f'Os número sorteados foram: ', end = '')

for n in tupla:
    print(f'{n} ',end = '')

print(f'\nO menor valor da tupla é {min(tupla)}')
print(f'O maior valor da tupla é {max(tupla)}')

