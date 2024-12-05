class Formas: 

	def __init__ (self, base = None, altura = None, radio = None):
		self.__base=base
		self.__altura=altura
		self.__radio=radio 

	def setBase(self, base):
		self.__base = base
	def calcularArea(self): 
		raise NotImplementedError("Subclases deben implementar este método")
	def calcularPerimetro(self):
		raise NotImplementedError("Subclases deben implementar este método")


class Cuadrado(Formas):
	def __init__(self, base, altura = None,radio = None):
		super().__init__(base)
	
	def calcularArea(self):
		return self.base** 2
	def calcularPerimetro(self):
		return self.base*4

class Rectangulo(Formas):
	def __init__(self,base,altura,radio = None):
		super().__init__(base, altura)
	def calcularArea(self): 
		return self.base * self.altura
	def calcularPerimetro(self):
		 return self.base*2 + self.altura*2

class Triangulo(Formas):
	def __init__(self, base,altura, radio= None):
		super().__init__(base,altura)
	def calcularArea(self):
		return (self.base * self.altura) / 2
	def calcularPerimetro(self):
		return(self.base+self.altura+((self.base ** 2 + self.altura**2)**(1/2)))

class Circulo():
	def __init__(self, radio):
		self.radio = radio
	def calcularArea(self):
		PI=3.14
		print(self.radio)
		return PI * (self.radio ** 2)
	def calcularPerimetro(self):
		PI=3.14
		return 2*(PI) * self.radio
