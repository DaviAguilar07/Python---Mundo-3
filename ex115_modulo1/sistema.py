from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo'

if not arquivo_existe(arq):
    criar_arquivo(arq)
#     print('Arquivo encontrado com sucesso!')
# else:
#     print('O arquivo não foi encontrado.')
#     criar_arquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])

    if resposta == 1:
        cabeçalho('Opção 1')
        # Listar as pessoas cadastradas
        lerarquivo(arq)
    elif resposta == 2:
        cabeçalho('Opção 2')
        # Cadastrando pessoas
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...')
        break
    else:
        print('Erro! Digite uma opção válida.')

    sleep(2)
