class CuentaBancaria:
	def __init__(self, numerocuenta, nombre, apellido):
		self.numerocuenta=numerocuenta
		self.nombre=nombre
		self.apellido=apellido
		self.saldo=100000 #saldo de inicio
		def depositar (self, cantidad):
			if cantidad > 0:
			self.saldo+=cantidad
			print (f"Se han depositado{cantidad}. Nuevo saldo: {self.saldo}")
			else: 
				print ("La cantidad depositada debe ser positiva.")

	def retirar (self, cantidad):
		if cantidad > 0:
			if cantidad <= self.saldo:
				self.saldo-=cantidad
				print (f"Se han retirando {cantidad}.Nuevo Saldo: {self.saldo}.")
			else: 
				print ("Fondos insuficientes para realizar el retiro.")
		else: 
			print ("La cantidad a retirar debe ser positiva")

	def versaldo (self):
		print (f"Saldo actual: {self.saldo}")
		



