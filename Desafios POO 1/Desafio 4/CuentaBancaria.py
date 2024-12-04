class CuentaBancaria:
	def __init__(self, numerocuenta, nombre, apellido):
		self.__numerocuenta=numerocuenta  #  __atributo esta en privado
										  #  _ protegidos las subclases y la misma
										  #    publicos todos tienen acceso
		self.__nombre=nombre
		self.__apellido=apellido
		self.__saldo=100000 #saldo de inicio
	



	def depositar (self, cantidad):
		if cantidad > 0:
			self.__saldo+=cantidad
			print (f"Se han depositado{cantidad}. Nuevo saldo: {self.__saldo}")
		else: 
			print ("La cantidad depositada debe ser positiva.")

	def retirar (self, cantidad):
		if cantidad > 0:
			if cantidad <= self.__saldo:
				self.__saldo-=cantidad
				print (f"Se han retirando {cantidad}.Nuevo Saldo: {self.__saldo}.")
			else: 
				print ("Fondos insuficientes para realizar el retiro.")
		else: 
			print ("La cantidad a retirar debe ser positiva")

	def versaldo (self):
		print (f"Saldo actual: {self.__saldo}")
		
	
	def __str__(self):
		return (f"Nro cuenta:{self.__numerocuenta}\nNombre:{self.__nombre} {self.__apellido}\nSaldo: {self.__saldo}")



