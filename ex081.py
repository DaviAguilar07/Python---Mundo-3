lista = []
cont = 0
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)

    cont += 1 #Contador de números

    r = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if r == 'N':
        break

lista.sort(reverse = True)

print(f'Foram digitados {cont} números.')
print(f'A lista é {lista}.')

if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
    
