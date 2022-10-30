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

