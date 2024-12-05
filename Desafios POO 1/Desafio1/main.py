"""
Persona. crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
Construye los siguientes métodos para la clase:

a. Un constructor, donde los datos pueden estar vacíos.

b. Los setters y getters para cada uno de los atributos. Hay que validar las
entradas de datos.

c. mostrar(): Muestra los datos de la persona.

d. esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

Además, crea en una aplicación de consola que permita al usuario crear un objeto
Persona y evaluar si es mayo o menor de edad..


"""
def main():
	nombre = input("ingrese nombre: ")
	ingreso = True
	while (ingreso):
		try:
			edad = int(input("ingrese edad: "))
		except
	DNI = int(input("ingrese DNI(sin puntos): "))
