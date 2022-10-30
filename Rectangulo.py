class Rectangulo:
    """
    Ejercicio de BOGADO NICOLÁS
    Crear una clase llamada Rectángulo, debe tener 2 atributos: altura y base
    el nombre del método será calcular área utilizando la fórmula:
    area = base * altura. Pero la base y la altura deben ser ingresadas por el usuario y los objetos deben ser tres
    """
    def __init__(self, base, altura):
        self.altura = altura
        self.base = base
    def area(self):
        return self.base * self.altura

altura = int(input('Ingrese la altura del rectángulo: '))
base = int(input('Ingrese la base del rectángulo: '))
area = Rectangulo(altura, base)
print(f'El área del rectángulo es: {area1.area():.2f}')

