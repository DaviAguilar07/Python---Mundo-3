def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


lista = [8, 6, 2, 1, 0, 4]
print(lista) # Antes de ser dobrada
dobra(lista) # Chama a função para dobrar
print(lista) # Imprime a lista dobrada
