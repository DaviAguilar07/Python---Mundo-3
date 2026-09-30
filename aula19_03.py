brasil = list()
estado = dict()

for c in range(0, 3):
    estado['uf'] = str(input('Digite o Estado: '))
    estado['silga'] = str(input('Digite a sigla: '))
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print(v, end = ' ')
