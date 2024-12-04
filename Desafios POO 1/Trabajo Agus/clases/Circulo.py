from Formas import Formas
class Circulo(Formas):
	def __init__(self,radio):
		super().__init__(radio)
	def calcularArea(self):
		PI=3.14
		return PI* self.radio **2
	def calcularPerimetro(self):
		PI=3.14
		return 2*(PI) * self.radio
