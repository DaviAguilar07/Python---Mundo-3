# galera = [['João', 40], ['Maria', 22], ['Luan', 34], ['Ronaldo', 25]]
#                0    1       0      1       0     1        0       1   dados
#                   0             1             2               3       galera
# print(galera[2])

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # Joga os dados para dentro da lista galera
    dado.clear() # Limpa os dados a cada iteração. Sem afetar o append.

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'{totmai} pessoas são maiores de idade.')
print(f'{totmen} pessoas são menores de idade.')
