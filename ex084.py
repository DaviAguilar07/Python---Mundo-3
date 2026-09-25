temp = list()
princ = list()
cont = 0
men = 0
mai = 0
while True:
    temp.append(str(input('Nome: '))) #temp[0]
    temp.append(int(input('Peso: ')))#temp[1]
    
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    cont += 1
    princ.append(temp[:]) #Joga a cópia do temp dentro da lista princ.
    temp.clear() #Limpa o temp.S

    r = str(input('Você quer continuar [S/N]? ')).upper().strip()[0]
    if r == 'N':
        break
    
print(f'Foram cadastradas {cont} pessoas.')
print(f'O maior peso foi {mai} Kg e foi de ', end = '')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}.')
print(f'O menor peso foi {men} Kg e foi de ', end = '')
for p in princ:
    if p[1] == men:
        print(f'{p[0]}.')
