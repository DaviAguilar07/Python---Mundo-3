numeros = list()
numero_par = list()
numero_impar = list()

while True:

    num = int(input('Digite um número: '))
    numeros.append(num)

    if num == 0:
        print('Número par.')
        numero_par.append(num)
    elif num % 2 == 0:
        print('Número par.')
        numero_par.append(num)        
    else:
        print('Número ímpar.')
        numero_impar.append(num)

    r = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if r =='N':
        break

print(f'A lista de números digitados é: {numeros}.')
print(f'A lista de número pares digitados é: {numero_par}.')
print(f'A lista de números ímpares digitados é: {numero_impar}.')
