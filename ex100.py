from random import randint
from time import sleep

def sortear(lista):
    print(f'Sorteando os 5 valores da lista: ',end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush = True)
        sleep(0.3)

def soma_par(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares da lista {lista}, é: {soma}.')


numeros = list()
sortear(numeros)
print()
soma_par(numeros)
