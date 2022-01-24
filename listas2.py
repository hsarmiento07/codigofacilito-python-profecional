from subprocess import list2cmdline


cursos = ['Python', 'Django', 'Flask']

cursos_tupal = tuple(cursos)
print(cursos_tupal)
print(type(cursos_tupal))

niveles = ('Basico', 'intermedio', 'Avanzado')

niveles_listas = list(niveles)
print(niveles_listas)
print(type(niveles_listas))