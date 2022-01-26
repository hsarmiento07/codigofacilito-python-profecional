# lambda <parametros> : <Cuerpo de la función>

funcion_grados = lambda grados : grados * 1.8 + 32

print(funcion_grados(10))

"""
sin_parametros = lambda : True
parametros_default = lambda p1=10, p2=20, p3=30 : p1 + p2 + p3
asterisco = lambda *args, **kwargs: len(args) + len(kwargs)
"""


#def centigrado_a_farhenheit(grados):
#    return grados * 1.8 + 32
#
#
#mi_funcion = centigrado_a_farhenheit
#
#print(type(mi_funcion))
#
#print(mi_funcion(10))