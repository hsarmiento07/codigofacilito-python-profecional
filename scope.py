# Scope
animal = 'León' # Variable global -> Función, Condicion o Ciclo

def imprimir_animal():
    global animal

    animal = 'Ballena' # Variable Local

    tipo = 'Mamifero' # Variable Local

    print(animal)
    print(id(animal))

imprimir_animal()

print(animal)
print(id(animal))