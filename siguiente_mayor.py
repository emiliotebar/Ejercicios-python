""">>> siguiente_mayor([5, 7, 3, 2, 8])
[7, 8, 5, 3, -1]

>>> siguiente_mayor([2, 3, 4, 5])
[3, 4, 5, -1]

>>> siguiente_mayor([1, 0, -1, 8, -72])
[8, 1, 0, -1, -1]
"""

l = [1, 0, -1, 8, -72]

def siguiente_mayor(lista):
    resultado = []
    mayor = max(lista)
    for element in lista:
        if element == mayor:
            resultado.append(-1)
        else:
            resultado.append(sorted(list(filter(lambda x: x > element, lista,)))[0])
    return resultado
   

print(siguiente_mayor(l))