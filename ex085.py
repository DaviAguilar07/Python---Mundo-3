pessoas = [[], []]

for c in range(0, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        pessoas[0].append(num)
    else:
        pessoas[1].append(num)


print(f'A lista de valores é {pessoas}.')
pessoas[0].sort()
print(f'A lista de valores pares é {pessoas[0]}.')
pessoas[1].sort()
print(f'A lista de valores impares é {pessoas[1]}.')
