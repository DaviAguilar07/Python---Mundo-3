lista = []
for pos in range(0, 5):
    lista.append(int(input(f'Insira o {pos + 1}° valor: ')))

for p, c in enumerate(lista):
    print(f'Na posição {p}, está o valor {c}.')

