""">>> acumulado([1, 5, 7])
[1, 6, 13]

>>> acumulado([1, 0, 1, 0, 1])
[1, 1, 2, 2, 3]

>>> acumulado([])
[]
"""

l = [1, 5, 7]

def acumulado(lista):
    lista_acumulada = []
    for i in range(len(lista)):
        if (i == 0):
            lista_acumulada.append(lista[i])
        else:
            lista_acumulada.append(lista_acumulada[i-1] + lista[i])
    return lista_acumulada




print(acumulado(l))