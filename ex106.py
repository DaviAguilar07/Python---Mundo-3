while True:
    frase = str(input('Função ou biblioteca> '))
    if frase.lower() == 'fim':
            """
            Finaliza o programa. Interrompendo o funcionamento do help interactive.
            """
            break    
    else:
         help(frase)
