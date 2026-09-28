from random import randint
lista = list()
jogos = list()
print('-'*30)
print('     Jogos da Mega-Sena          ')
print('-'*30)

quant = int(input('Quantos jogos você quer jogar? '))
tot = 1
cont = 0
while tot <= quant:
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-'*3, f'O sorteio de {quant} jogos', '-'*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')

