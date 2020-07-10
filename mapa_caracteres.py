# Ejemplos
#>>> mapa_caracteres('abcd')
#[0, 1, 2, 3]
#>>> mapa_caracteres('aabbb')
#[0, 0, 1, 1, 1]
#>>> mapa_caracteres('zagzdaa')
#[0, 1, 2, 0, 3, 1, 1]
#>>> mapa_caracteres('baaacbb')
#[0, 1, 1, 1, 2, 0, 0]

cadena = 'baaacbb'

def mapa_caracteres(cadena):
    contador = 0
    list = []
    dicc = {}
    
    for c in cadena:
        if c not in dicc:
            dicc[c] = contador
            contador = contador + 1
        list.append(dicc[c])

    print(list)

mapa_caracteres(cadena)