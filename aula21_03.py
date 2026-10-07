# Escopo de variáveis: Dessa maneira, os valores do escopo local e global são diferentes
def valor():
    # Escopo local
    n1 = 4
    print(f'O valor de n1 dentro vale: {n1}')

# Escopo global
n1 = 2
valor()
print(f'O valor de n1 fora vale: {n1}')

print('-='*30)
# Escopo de variáveis: Dessa maneira, ocorre apenas a troca de valor da variável golbal
def valor2():
    # Escopo local
    global a1
    a1 = 8
    print(f'O valor de a1 dentro é: {a1}')

# Escopo global
a1 = 15
print(f'Valor de a1 fora vale: {a1}') # Valor de a1 antes de chamar a função
valor2() # Chama a função (troca o valor de a1)
print(f'Após a chamada da função: ', end='')
print(f'Valor de a1 fora vale: {a1}') # Valor da variável global a1 é trocada
