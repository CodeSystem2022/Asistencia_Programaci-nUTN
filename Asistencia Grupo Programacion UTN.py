class Cubo:
    """"
    Ejercicio Cubo: Joaquín Zabala / Usuario en YT: Joaquín Zabala

    Crear la clase Cubo con los atributos, alto, ancho, profundidad, con un metodo
    que se llame calcular_volumen que tendra la formula:
    volumen = ancho * altura * profundidad
    que el usuario ingrese los valores.
    """
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad

alto = int(input(f"Digite el numero para el alto del cubo: "))
ancho = int(input(f"Digite el numero para el ancho del cubo: "))
profundidad = int(input(f"Digite el numero para la profundidad del cubo: "))

cubo1 = Cubo(alto, ancho, profundidad)

print(f"El volumen del cubo es: {cubo1.calcular_volumen()}")

"""
----------------------------------------------------------------------------------------------------
"""

class Artimetica:
    """
    Ejercicio de AYELEN CABRAL
    El nombre de este tipo de comentario es: DocString, esto es documentación de la clase de Python
    vamos a hacer en ésta clase algunas operaciones de: suma, resta, multiplicación y más
    """
    def __init__(self, oprandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
        # métooo para sumar
    def sumar(self):
        return self.operandoA + self.operandoB
    def restar(self):
        return self.operandoA - self.operandoB
    def multiplicar(self):
        return self.operandoA * self.operandoB
    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Artimetica(7, 9) # le pasamos los argumentos para los operando
print(aritmetica1.sumar())
print(f'La resta de los números es: {aritmetica1.restar()}')
print(f'La multiplicación de los números es: {aritmetica1.multiplicar()}')
print(f'La división de los números es: {aritmetica1.dividir():.2f}')

"""
----------------------------------------------------------------------------------------------------
"""

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
