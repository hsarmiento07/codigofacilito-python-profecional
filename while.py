numero = 1234
contador_digitos = 0

while numero >= 1:
    #contador_digitos = contador_digitos + 1
    contador_digitos += 1

    numero = numero / 10
else:
    print('Fin de el ciclo While')

print(contador_digitos)

#contador = 1
#
#while contador <= 10:
#    print(contador)
#
#    contador = contador + 1