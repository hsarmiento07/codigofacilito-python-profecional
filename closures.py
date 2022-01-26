e = 'e' # Variables global

def funcion_principal():
    a = 'a'# variables locales
    b = 'b'

    def funcion_anidada():
        c = 'c' # variables locales

        nonlocal b
        b = 'Cambio de valor'

        print(a)
        print(b)
        print(id(b))

        print(e)

    funcion_anidada()
    # print(c)
    print(b)
    print(id(b))


funcion_principal()