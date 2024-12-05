class Formas: 

	def __init__ (self, base, altura, radio):
		self.base=base
		self.altura=altura
		self.radio=radio 

	def calcularArea(self): 
		raise NotImplementedError("Subclases deben implementar este método")
	def calcularPermimetro(self):
		raise NotImplementedError("Subclases deben implementar este método")

    