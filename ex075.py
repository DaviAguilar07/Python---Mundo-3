num = (int(input('Insira um valor: ')), 
       int(input('Insira um valor: ')),
    int(input('Insira um valor: ')), 
    int(input('Insira um valor: ')))

print(f'Os números digitados foram {num}.')

print(f'O número 9 apareceu {num.count(9)} vezes.')

if 3 in num:
    print(f'O número 3 foi digitado na {num.index(3) + 1}° posição.')
else:
    print(f'O número 3 não foi digitado.')

print(f'Os números pares são: ', end = '')

for c in num:
    if c % 2 == 0:
        print(f'{c}', end = ' ')
