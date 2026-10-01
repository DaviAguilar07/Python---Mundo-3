from random import randint
from operator import itemgetter
jogadores = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6), 'Jogador 3': randint(1, 6),
              'Jogador 4': randint(1, 6)}

print(f'---- Valores sorteados ----')
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')

print(f'---- Ranking dos jogadores ----')
ranking = sorted(jogadores.items(), key = itemgetter(1), reverse = True) # Retorna como uma lista

for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]} pontos')
