# def valor(*num):
#     for valor in num:
#         print(f'{valor} ',end='')
#     print('fim')


# valor(5, 9, 10)
# valor(2, 4, 6)
# valor(15, 6, 78)

# Desempacotamento
def valor(*num):
    print(f'Foram inseridos tais valores: {num}.')
    print(f'Inseriram {len(num)} elementos.')


valor(15, 21, 33)
valor(80, 2, 10, 12, 13, 22)
valor(14, 22, 13, 70, 30, 55)
