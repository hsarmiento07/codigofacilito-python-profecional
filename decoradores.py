def funcion_a(funcion_b):

    def funcio_c(*args, **kwargs):
        print('>>> Antes del llamado.')

        resultado = funcion_b(*args, **kwargs)

        print('>>> Despues del llamado.')

        return resultado

    return funcio_c


@funcion_a
def suma(numero_1, numero_2):
    return numero_1 + numero_2

resultado = suma(15, 70)
print(resultado)