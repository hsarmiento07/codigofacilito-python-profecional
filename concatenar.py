nombre = 'Howerd Eduardo'
apellido = 'Sarmiento'

# nombre_completo = 'Mr.' + nombre + ' ' + apellido + '.'

# nombre_completo = 'Mr. %s %s %s.' %(nombre, apellido, 'Cordero')

#nombre_completo = 'Mr. {nombre} {apellido} {segundo_apellido}.'.format(
#    nombre=nombre,
#    apellido=apellido,
#    segundo_apellido='cordero'
#    )

nombre_completo = f'Mr. {nombre} {apellido} {10 * 20}'

print(nombre_completo)