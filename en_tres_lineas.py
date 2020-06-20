cadena = list(set(input("Introduce secuencia de palabras").upper().split()))
cadena.sort()
print(' '.join(cadena))