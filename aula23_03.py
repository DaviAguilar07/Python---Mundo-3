try: # Tenta realizar tal operação
    a = float(input('Insira um número: '))
    b = float(input('Insira um número: '))
    r = a / b
except Exception as error: # Caso ocorra algum erro, aparecerá essa mensagem
    print(f'Infelizmente tivemos um problema com o {error.__class__}') # Imprimirá especificamente onde está o erro
else: # Caso não tenha dado erro, aparecerá essa mensagem
    print(f'O resultado é: {r}')
finally: # Essa mensagem ocorrerá sempre, independente se deu erro ou não
    print(f'Volte sempre!') # É útil em situações em que é necessário fechar um banco de dados
