#Ejercicio Persona - Eduardo Montes
class Persona: # Creamos una clase.
    def __init__(self, nombre, apellido, edad): # Se lo llama método Init Dunder.
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrarDetalle(self):
        print(f'Persona: {self.nombre}{self.apellido}{self.edad}')
persona1 = Persona('Edu', 'Montes', '46') # Necesitamos enviar argumentos.
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

print(f'El objeto1 de la clase persona es: {persona1.nombre} {persona1.apellido} y su edad es {persona1.edad}')

persona2 = Persona ('Lorena', 'Coronel', 44)
print(f'El objeto2 de la clase persona es: {persona2.nombre} {persona2.apellido} y su edad es {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto1 modificado de la clase persona es: {persona1.nombre} {persona1.apellido} y su edad es {persona1.edad}')

# Los atributos son: características.
# Los métodos son: el comportamiento que van a tener los objetos (acciones).

persona1.mostrarDetalle()
persona2.mostrarDetalle()

