nombre = 'Howerd Eduardo'
apellido = 'Sarmiento'

# nombre_completo = 'Mr.' + nombre + ' ' + apellido + '.'

# nombre_completo = 'Mr. %s %s %s.' %(nombre, apellido, 'Cordero')

nombre_completo = 'Mr. {nombre} {apellido} {segundo_apellido}.'.format(
    nombre=nombre,
    apellido=apellido,
    segundo_apellido='cordero'
    )

print(nombre_completo)