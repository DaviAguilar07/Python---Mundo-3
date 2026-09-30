pessoas = {'nome': 'Tobias', 'idade': 30, 'sexo': 'M'}

pessoas['nome'] = 'Ronaldo' # Mudou o nome para Ronaldo
del pessoas['sexo'] # Deleta o índice e o valor do dicionário
pessoas['peso'] = 80.0 # Adicona o elemento peso no dicionário

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

print(pessoas.keys()) # Irá imprimir os índices/chave do dicionário

print(pessoas.items())

print('-'*30)
for k, v in pessoas.items():
    print(f'{k}: {v}') # Irá imprimir os índices e os valores do dicionário

print('-'*30)

for k in pessoas.keys():
    print(f'{k}') # Irá imprimir as chaves/índices do dicionário

print('-'*30)

for k in pessoas.values():
    print(f'{k}') # Irá imprimir os valores do dicionário
