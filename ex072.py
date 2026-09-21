extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze','doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input("Digite um número inteiro (0 a 20): "))

    if 0 <= num <= 20:
        print(f"A escrita por extenso é {extenso[num]}.\n")
        
        decisao = ' '
        while decisao not in 'SN':
            decisao = str(input("Você quer continuar [S/N] ? ")).upper().strip()[0]
        
        if decisao == 'N':
            break
    else:
        print("Tente novamente.", end=' ')
