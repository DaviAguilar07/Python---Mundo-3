from datetime import datetime

nome = str(input('Digite o seu nome: '))
ano_de_nasc = int(input('Digite o ano de nascimento: '))
clt = int(input('Digite o número de sua carteira de trabalho (Digite 0, caso não tenha): '))

if clt != 0:
    ano_de_contrataçao = int(input('Ano de contratação: '))
    salario = float(input('Salário: R$'))

    cadastro1 = {'Nome': nome, 'Ano de nascimento': ano_de_nasc, 
             'CLT': clt, 'Ano de contratação': ano_de_contrataçao, 'Salario': salario}
    
else:
    cadastro1 = {'Nome': nome, 'Ano de nascimento': ano_de_nasc, 
             'CLT': clt}

cadastro1['Idade'] = (datetime.today().year - ano_de_nasc)

if clt != 0:
    cadastro1['Aposentadoria'] = (cadastro1["Idade"] + 35)
    cadastro1['Ano de aposentadoria'] = (cadastro1["Ano de contratação"] + 35)

print('=-'*5, 'Resultado', '=-'*5)
for i, v in cadastro1.items():
    print(f'{i} = {v}')
    