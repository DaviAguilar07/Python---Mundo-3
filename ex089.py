lista = list()
princ = list()

while True:
    nome = str(input('Nome: '))
    lista.append(nome)
    nota1 = float(input('Nota 1: '))
    lista.append(nota1)
    nota2 = float(input('Nota 2: '))
    lista.append(nota2)

    media = (nota1 + nota2) / 2
    lista.append(media)

    princ.append(lista[:])
    lista.clear()

    r = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if r == 'N':
        break

for i, c in enumerate(princ):
     print(f'|N° {i}| Aluno: {c[0]:.2}| Nota 1: {c[1]:.2}| Nota 2: {c[2]:.2}| Média: {c[3]}')

