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

"""
----------------------------------------------------------------------------------------------------
"""
class Vehiculo:
    """
    Ejercicio de Nadia Cruz
    Definir una clase padre llamada Vehiculo y dos clases hijas llamadas
    Auto y Bicicleta, las cuales heredaran de la clase padre Vehiculo.La clase
    padre debe tener los siguientes atributos y métodos:
    Vehiculo (clase padre)
    -ATRIBUTOS(COLOR,RUEDAS)
    -Métodos (__init__() y __str__())

    Auto(clase hija de vehiculo)
    -Atibutos( velocidad(km/hr))
    -Métodos (__init__() y __str__())
    Bicicleta(clase hija de Vehiculo)
    -Atributos(tipo(urbana /montaña/etc.)
    -Métodos (__init__() y __str__())
    Crear un objeto de cada clase

    """

    # Creación clases y métodos
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "Color: " + self.color + ", Ruedas: " + str(self.ruedas)


class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__()+ ', Velocidad(km/hr): ' + str(self.velocidad)


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__()+ 'Tipo: ' + self.tipo


# Creación objetos

vehiculo = Vehiculo("Rojo", 5)

camioneta = Auto("Negro", 4, 140)

bicicleta = Bicicleta("Blanca", 2, "Montaña")

print(vehiculo)
print(camioneta)
print(bicicleta)
"""
----------------------------------------------------------------------------------------------------
"""
#Ejercicio de Camila Gónzalez
class FiguraGeometrica:
    def __init__(self,ancho, alto):
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self,ancho):
        self._alto = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self,alto):
        self._alto = alto

    def __str__(self):
        return f'FiguraGeometrica [ Ancho : {self._ancho}, Alto: {self._alto}]'
    
    class Color:
    def __init__(self,color):
        self.color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,color):
        self._color = color

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'
