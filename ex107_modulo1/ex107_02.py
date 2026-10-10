from ex107_modulo1 import moeda

num = float(input('Informe o preço: R$'))
print(f'A metade de {num}, é {moeda.metade(num)}')
print(f'O dobro de {num}, é {moeda.dobro(num)}')
print(f'Aumentando 10% de {num}, fica: {moeda.aumentar(num)}')
print(f'Diminuindo 13% de {num}, fica: {moeda.diminuir(num)}')
