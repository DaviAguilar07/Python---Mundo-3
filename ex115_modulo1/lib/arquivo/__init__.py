from lib.interface import *

def arquivo_existe(nome):
    try:
        a = open(nome, 'rt') # read text
        a.close()
    except FileNotFoundError: # Caso não encontre 
        return False
    else: 
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+') # Escreve um arquivo de texto, caso não exista, ele cria um arquivo
        a.close(nome)
    except:
        print('Houve algum erro na criação do arquivo.')
    else:
        print(f'Arquivo {a} criado com sucesso!')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1].replace(';', '')
            print(f'{dado[0]:<30}{dado[1]:>3}anos')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at') # Append text. Adicionar texto
    except:
        print(f'Houve algum ERRO na abertura de um arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n') # Escreva nome e idade
        except:
            print('Houve um erro na hora de imprimir os dados.')
        else:
            print(f'O nome {nome} foi adicionado com sucesso.')
            a.close()

