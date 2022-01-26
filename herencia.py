class Animal:

    def comer(self):
        print('el animal come.')


class Mascota(Animal):

    def comer(self):
        super().comer()
        print('la mascota come.')

class Felino:

    def cazar(self):
        print('el Felino caza.')

class Gato(Mascota, Felino):

    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        super().comer()
        print(f'{self.nombre} come.')

patricio = Gato('Patricio')

patricio.comer()
