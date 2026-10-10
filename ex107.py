from ex107_modulo1 import dobro, diminuir, aumentar, metade

num = float(input('Informe o preço: R$'))
print(f'A metade de {num}, é {metade(num)}')
print(f'O dobro de {num}, é {dobro(num)}')
print(f'Aumentando 10% de {num}, fica: {aumentar(num)}')
print(f'Diminuindo 13% de {num}, fica: {diminuir(num)}')
