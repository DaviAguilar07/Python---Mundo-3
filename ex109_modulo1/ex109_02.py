import moeda

num = float(input('Informe o preço: R$'))
print(f'A metade de {moeda.moeda(num)}, é {moeda.metade(num, True)}')
print(f'O dobro de {moeda.moeda(num)}, é {moeda.dobro(num, True)}')
print(f'Aumentando 10% de {moeda.moeda(num)}, fica: {moeda.aumentar(num, True)}')
print(f'Diminuindo 13% de {moeda.moeda(num)}, fica: {moeda.diminuir(num, True)}')
