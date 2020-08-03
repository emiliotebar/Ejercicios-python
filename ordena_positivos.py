"""
>>> ordena_positivos([6, 3, -2, 5, -8, 2, -2])
[2, 3, -2, 5, -8, 6, -2]
>>> ordena_positivos([6, 5, 4, -1, 3, 2, -1, 1])
[1, 2, 3, -1, 4, 5, -1, 6]
>>> ordena_positivos([-5, -5, -5, -5, 7, -5])
[-5, -5, -5, -5, 7, -5]
>>> ordena_positivos([])
[]
"""

l = [6, 3, -2, 5, -8, 2, -2]

def ordena_positivos(lista):
    lista1 = sorted(list(filter(lambda x: x >0, lista)))
    index = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            lista[i] = lista1[index]
            index = index + 1
    return lista
    

 
print(ordena_positivos(l))