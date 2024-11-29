"""
Persona. crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
Construye los siguientes métodos para la clase:

a. Un constructor, donde los datos pueden estar vacíos.

b. Los setters y getters para cada uno de los atributos. Hay que validar las
entradas de datos.

c. mostrar(): Muestra los datos de la persona.

d. esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
"""

class Persona:
	#constructores
	def __init__(self, nombre, edad, DNI):
		self.__nombre = nombre
		self.__edad = edad
		self.__DNI = DNI

	def __init__(self):
		self.__nombre = None
		self.__edad = None
		self.__DNI = None
	# getters
	def getNombre(self):
		return self.nombre
	def getEdad(self):
		return self.edad
	def getDni(self):
		return self.DNI
	# setters
	def setNombre(self, nombre):
		self.__nombre = nombre
	def setEdad(self, edad):
		self.__edad = edad
	def setDni(self, DNI):
		self.__DNI = DNI

	# Metodos
	def mostrar(self):
		print(f"Nombre: {self.__nombre}\nEdad: {self.__edad}\nDNI: {self.__DNI}")

	def esMayorDeEdad(self):
		return (self.__edad >= 18)


