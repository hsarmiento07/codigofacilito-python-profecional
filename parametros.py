from cmath import pi


def area_circulo(radio, pi=3.14):
    return pi * (radio ** 2)

resultado = area_circulo(radio=10, pi=3.141592)
print(resultado)