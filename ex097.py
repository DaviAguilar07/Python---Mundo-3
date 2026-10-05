def escreva(txt):
    print('-'*30)
    print(f'        {txt}')
    print('-'*30)

escreva('Olá mundo!')
print()
frase = str(input('Insira uma frase para o letreiro: '))
escreva(frase)