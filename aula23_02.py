try:
    a = float(input('Insira um número: '))
    b = float(input('Insira um número: '))
    r = a / b
except (ValueError, TypeError): # Imprimirá caso dê algum erro de tipo ou de valor na inserção do usuário.
    print(f'O usuário inseriu um tipo de valor inválido.')
except ZeroDivisionError: # Imprimirá caso o usuário dividir algum valor por zero.
    print(f'Uma divisão por zero é inválida.')
except KeyboardInterrupt: # Imprimirá caso o usuário deixar a inserção vazia.
    print(f'O usuário não inseriu valor.')
except Exception as error:
    print(f'O erro encontrado foi: {error.__cause__}')
else: 
    print(f'O resultado é: {r:.2f}')
finally:
    print('Volte sempre!')
