def pares():
    for numero in range(0, 100, 2):
        yield numero

        print('Se reanuda la ejecucion')

generador = pares()

while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print('el generador finalizo.')
        break