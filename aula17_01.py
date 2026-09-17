lista = [5, 3, 4, 8]
lista[2] = 7
# len(lista)
# lista.pop(0) Só o pop, vai eliminar o ultimo. Se colocar a posição dentro do parentese ele elimina o valor que está nessa posição.
# lista.remove(3)

lista.append(15) #Vai adicionar o valor 15 no final.
lista.insert(3, 15) #Vai adicionar o valor 15 na posição 3.

if 5 in lista:
    lista.remove(5)
else:
    print('Não encontrei o número 5.')

# lista.sort() Deixa de forma crescente.
# lista.sort(reverse = True) Deixa de forma decrescente.

print(lista)
