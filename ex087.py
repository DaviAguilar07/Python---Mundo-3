matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somatotal = 0
maior = menor = 0
soma3coluna = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f'Insira um valor para a posição [{l}, {c}]: ')))

print(f'-='*30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end = '')

        if matriz[l][c] % 2 == 0:
            somatotal += matriz[l][c] #Calculando a soma de todos os valores dentro da matriz.
    print()

print(f'A soma de todos os valores é: {somatotal}.')

#Calculando a soma de todos os valores da terceira coluna.
for l in range(0, 3):
    soma3coluna += matriz[l][2]
print(f'A soma de todos os valores da terceira coluna é: {soma3coluna}.')

#Calculando o maior e menor da segunda linha.
for c in range(0, 3):
    if c == 0:
                if matriz[1][0]:
                    maior = menor = matriz[1][0]
                else:
                    if matriz[1][c] < menor:
                        menor = matriz[1][c]
    
                    if matriz[1][c] > maior:
                        maior = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior}.')
