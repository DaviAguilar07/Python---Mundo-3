ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media]) # Organiza como os dados ficarão dentro da lista.
#                   0          1           2
    r = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if r == 'N':
        break

print('-='*30)
print(f'{'N°':<4} {'Nome':<5} {'Média':>8}')
print('-'*26)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.2f}') # Imprime o N°, Nome e Média. Como cabeçalho.

while True:
    print('-'*35)
    opc = int(input('Mostrar a nota de qual aluno (digite 999 para encerrar): ')) # Indicar qual aluno o usuário quer saber a nota.

    if opc == 999:
        print('Encerrando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}.')

print('Volte sempre!')
