""">>> cuadrado(0)
[]
>>> cuadrado(1)
[[1]
>>> cuadrado(3)
[
    [3, 3, 3],
    [3, 3, 3],
    [3, 3, 3]
]
>>> cuadrado(5)
[
    [5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5]
]
"""

def cuadrado(n):
    return [[n] * n] * n

def cuadrado2(n):
    return [[n for _ in range(n)] for _ in range(n)]

def run():

    numero = int(input('Introduce un número '))
    if numero < 0:
        print("El número debe ser mayor que 0")
        numero = int(input('Introduce un número '))
       
    lista = cuadrado(numero)
    for fila in lista:
        print(fila)

    """lista = cuadrado2(numero)
    for fila in lista:
        print(fila)"""

if __name__ == '__main__':
    run()