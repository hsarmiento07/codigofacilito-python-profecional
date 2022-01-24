diccionario = {'a': 1, 'b': 2, 'c':3, 'd': 4}

print('a' in diccionario)


valor = diccionario.get('z', None)
print(valor)

valor_2 = diccionario.setdefault('e', 5)
print(valor_2)

print(diccionario)


# get
# setdefault
"""
valor = diccionario['a']
print(valor)
"""