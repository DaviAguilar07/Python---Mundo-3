brasileirao = ('Palmeiras', 'Flamengo', 'Athletico-Pr', 'Fluminense', 'Bahia', 'Cruzeiro', 'Coritiba', 'Atletico-Mg', 'Bragantino', 'Corinthians', 'São Paulo', 'Botafogo', 'Vitória', 'Santos', 'Gremio', 'Mirassol', 'Vasco da Gama', 'Internacional', 'Remo', 'Chapecoense')


print("A tabela do brasileirão é: {}".format(brasileirao))

print("-"*30)

print("Os cinco primeiros times do Brasileirão, são: ", end  = '')
print(brasileirao[1:6])

print('-'*30)

print("A zona de rebaixamento é: ", end = '')
print(brasileirao[-4:])

print('-'*30)

print('Em ordem alfabética: {}'.format(sorted(brasileirao)))

print('-'*30)

print('A chapecoense está na {}° posição.'.format(brasileirao.index('Chapecoense') + 1))
