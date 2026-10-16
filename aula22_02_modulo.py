from aula22_01_modulo_pt2 import fatorial, dobro, triplo, soma # Usando o __init__ dentro da pasta. Facilita a importação.
num = int(input('Insira um número para saber seu fatorial: '))
fat = fatorial(num)
print(f'O número é {num} e seu fatorial é {fat}')
print(f'O dobro do número é {dobro(num)}')
print(f'O triplo do número é {triplo(num)}')
print(f'A somando o {num} por 2, fica {soma(num)}')
