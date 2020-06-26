cadena = input('Introduce una cadena de texto  > ')

dic = dict()

for caracter in cadena:
    if caracter in dic.keys():
        dic[caracter] = dic[caracter] + 1
    else:
        dic[caracter] = 1

for k in dic.keys():
    print(f'{k}: {dic[k]}')