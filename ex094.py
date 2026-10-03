cadastrados = list()
pessoas = dict()
mulheres = list()
idades = list()
pessoas_acima_media = list()
while True:
    pessoas['Nome'] = str(input('Nome: '))
    pessoas['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    pessoas['Idade'] = int(input('Idade: '))
    cadastrados.append(pessoas.copy()) # O .copy() ajuda a realizar cópias e inserir na lista de cadastrados

    if pessoas['Sexo'] == 'F':
        mulheres.append(pessoas.copy())

    r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if r == 'N':
        break

for k, v in enumerate(cadastrados):
    idades.append(cadastrados[k]['Idade']) #Recolhe todas as idades da lista cadastro e insere na lisa de idades

media = (sum(idades)) / len(idades) # Faz o cálculo da média das idades

for k, v in enumerate(cadastrados):
    if cadastrados[k]['Idade'] > media:
        pessoas_acima_media.append(cadastrados[k]) # Analisa quais são as idades acima da média e insere na lista
                                                    # pessoas_acima_media todas as informações dessas pessoas

print('-='*10, 'Resultado', '-='*10)
print(f'{len(cadastrados)} pessoas cadastradas.')
print(f'A média de idade é de: {media:.2f} anos')
print(f'Mulheres na lista: {mulheres}')
print(f'Pessoas com idade acima da média: {pessoas_acima_media}')
