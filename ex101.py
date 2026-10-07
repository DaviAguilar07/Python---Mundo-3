from datetime import date

def voto(idade):
    if idade >= 18:
        return f'Com {idade} anos: Voto obrigatório!'
    elif 16 <= idade:
        return f'Com {idade} anos: Voto opcional!'
    else:
        return f'Com {idade} anos: Não vota!' 


ano_nasc = int(input('Informe o ano de nascimento: '))
idade = (date.today().year - ano_nasc)

resp = voto(idade)
print(f'{resp}')
