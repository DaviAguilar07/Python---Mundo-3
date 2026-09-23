sequencia =  ('anzol', 'pesca', 'peixe', 'barco')


for p in sequencia:
    print(f'\nNa palavra {p} temos ', end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra} ', end = '')
