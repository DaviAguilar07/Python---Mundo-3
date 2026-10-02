jogador = dict()
gol = list()

# Processamento dos dados
jogador['Nome'] = str(input('Digite o nome do jogador: '))
jogador['Jogos'] = int(input('Digite a quantidade de jogos que ele jogou: '))

for g in range(jogador["Jogos"]):
    golos = int(input(f'Digite a quantidade de gols que ele marcou na {g+1}° partida: '))
    gol.append(golos)

jogador['Gols'] = gol
jogador['Total de gols'] = sum(gol)

# Resultados
print('-='*10, 'Resultado 1', '-='*10)
print(jogador)

print('-='*10, 'Resultado 2', '-='*10)
print(f'O nome do jogador é: {jogador["Nome"]}.')
print(f'A quantidade de jogos do jogador é: {jogador["Jogos"]}.')
print(f'O total de gols marcados é: {jogador["Total de gols"]}.')
print(f'A estatística de gol é: {jogador["Gols"]}.')

print('-='*10, 'Resultado 3', '-='*10)
print(f'{jogador["Nome"]} jogou {jogador["Jogos"]} partidas')
for k, v in enumerate(jogador['Gols']):
    print(f'Na {k+1}° partida ele marcou {v} gols.')
