calificacion =  int(input("ingrese un numero: "))

if calificacion == 10:
    print('Felicidades, aprobaste la materia con una calificacion perfecta')
elif calificacion == 9 or calificacion == 8:
    print('Felizidades, aprobaste la materia  ')
elif calificacion == 7 or calificacion == 6:
    print('aprobaste la materia')
else:
    print('Reprobaste la materia')