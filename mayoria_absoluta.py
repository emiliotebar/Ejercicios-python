""">>> mayoria_absoluta(['A', 'A', 'B'])
'A'
>>> mayoria_absoluta(['A', 'A', 'A', 'B', 'C', 'A'])
'A'
>>> mayoria_absoluta(['A', 'B', 'B', 'A', 'C', 'C'])
None
"""

def mayoria_absoluta(votos):
    dicc = {}
    mitad = len(votos) / 2

    for voto in votos:
        if voto not in dicc:
            dicc[voto] = 1
        else:
            dicc[voto] = dicc[voto] + 1
            if dicc[voto] > mitad:
                return voto
    return None

print(mayoria_absoluta(['A', 'A', 'A', 'B', 'C', 'A']))

