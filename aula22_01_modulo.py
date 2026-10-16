import aula22_01_modulo_pt2.aula22_01_modulo as aula22_01_modulo # 1° maneira de importar
from aula22_01_modulo_pt2 import aula22_01_modulo_soma as somado # 2° maneira de importar
num = int(input('Insira um número para saber seu fatorial: '))
fat = aula22_01_modulo.fatorial(num)
print(f'O número é {num} e seu fatorial é {fat}')
print(f'O dobro do número é {aula22_01_modulo.dobro(num)}')
print(f'O triplo do número é {aula22_01_modulo.triplo(num)}')
print(f'A somando o {num} por 2, fica {somado.soma(num)}')
