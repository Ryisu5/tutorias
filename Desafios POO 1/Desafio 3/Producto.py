class Producto:
	def __init__(self, Nombre,Precio):
		self.Nombre=Nombre
		self.Precio=Precio
		self.Stock=0

	def actualizarStock(self, cantidad):
    # que cuente la cantidad de prendas que hay
        self.Stock += cantidad
    def calcularinventario (self):
    # que sume el stock que hay en el deposito
        return self.Stock * self.Precio
    def verdatos(self):
    # que vea los datos que tiene guardados
        return f"Nombre:{self.Nombre}, Precio:{self.Precio}, Stock:{self.Stock}"


