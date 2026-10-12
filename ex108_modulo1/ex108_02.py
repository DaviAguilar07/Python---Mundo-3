import moeda

num = float(input('Informe o preço: R$'))
print(f'A metade de {moeda.moeda(num)}, é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)}, é {moeda.moeda(moeda.dobro(num))}')
print(f'Aumentando 10% de {moeda.moeda(num)}, fica: {moeda.moeda(moeda.aumentar(num))}')
print(f'Diminuindo 13% de {moeda.moeda(num)}, fica: {moeda.moeda(moeda.diminuir(num))}')
