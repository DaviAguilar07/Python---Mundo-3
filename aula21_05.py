# Usando o return na função
def fatorial(num=1):
    f = 1
    for i in range(num, 0, -1):
        f *= i
    return f

r1 = fatorial(5)
r2 = fatorial(6)
r3 = fatorial(7)
print(f'Os valores dos fatorias são {r1}, {r2} e {r3}.')
