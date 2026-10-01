nome = str(input('Digite o seu nome: '))
media = float(input('Digite sua media: '))

if media >= 7:
    dici1 = {'Nome': nome, 'Media': media, 'Situação': 'Aprovado'}
else:
    dici1 = {'Nome': nome, 'Media': media, 'Situação': 'Reprovado'}

print(dici1)
print('-'*4, 'Resultado', '-'*4)
print(f'O nome é {dici1["Nome"]}.')
print(f'A média é {dici1["Media"]}.')
print(f'Está {dici1["Situação"]}')


print(f'-'*4, 'Resultado 2.0', '-'*4)
for k,v in dici1.items():
    print(f'{k} = {v}')
    