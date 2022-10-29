class Cubo:
    """"
    Ejercicio Cubo: Joaquín Zabala

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