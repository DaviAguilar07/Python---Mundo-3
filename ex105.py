def boletim(*num, sit=False):
    if sit == True:
        media = (sum(num))/len(num)
        if media>=7:
            situaçao = 'Boa'
        elif media>=5:
            situaçao = 'Mediano'
        else:
            situaçao = 'Ruim'

        dici1 = {'Quantidade de notas': len(num), 'Maior nota': max(num), 'Menor nota': min(num),
                  'Média da turma': media, 'Situação': situaçao}

    else:
        dici1 = {'Quantidade de notas': len(num), 'Maior nota': max(num), 'Menor nota': min(num),
                          'Média da turma': media}
    
    return dici1


resp = boletim(8.2, 5.6, 9.0, 8.0, sit=True)
print(resp)
