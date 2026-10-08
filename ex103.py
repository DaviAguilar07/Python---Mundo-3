def jogador(nome='<Desconhecido>', gols=0):
    print(f'{nome} fez {gols} gols no campeonato.')


nome_jogador = str(input('Insira o nome do jogador: '))
gols_jogador = str(input('Insira a quantidade de gols do jogador: '))
if gols_jogador.isnumeric():
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0

if nome_jogador.strip() == '':
    jogador(gols=gols_jogador)
else:
    jogador(nome_jogador, gols_jogador)
