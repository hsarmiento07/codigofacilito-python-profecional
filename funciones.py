def suma(n1, n2):
    return n1 + n2, 'La funcion retorna 2 valores'



numero_uno = int(input('Ingresa el primer número entero: '))
numero_dos = int(input('Ingresa el segundo número entero: '))

resultado, mensaje = suma(numero_uno, numero_dos)
print('El resultado: ', resultado)
print(mensaje)