# Ejemplo 1 
    #>>> d = {'Valencia': 794000, 'Salamanca': 144000, 'Cádiz': 116000, 'Madrid': 3200000}
    #>>> ordena_ciudades(d)
    #['Madrid', 'Valencia']
# Ejemplo 2
d = {'Cuautitlán': 108000, 'C. México': 8800000, 'Zamora': 141000, 'Guadalupe': 673000}
    #>>> ordena_ciudades(d)
    #['C. México', 'Guadalupe']
# Ejemplo 3
    #d = {'La Plata': 860000, 'Rosario': 1350000, 'Quilmes': 230000, 'Buenos Aires': 3000000}
    #>>> ordena_ciudades(d)
    #['Buenos Aires', 'Rosario', 'La Plata', 'Quilmes']


def ordena_ciudades(d):
    return sorted((k for k, v in d.items() if v >= 200000), key=lambda x: d[x], reverse=True)

print(ordena_ciudades(d))