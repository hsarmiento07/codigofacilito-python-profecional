class Ciculo:

    pi = 3.141592

    @classmethod
    def area(cls, radio):
        return cls.pi * (radio ** 2)

resultado = Ciculo.area(14)
print(resultado)