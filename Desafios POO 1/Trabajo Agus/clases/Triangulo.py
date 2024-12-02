class Triangulo(Formas):
	def __init__(self, base,altura):
		super().__init__(base,altura)
	def calcularArea(self):
		return (self.base * self.altura) / 2
    def calcularPermimetro(self):
    	return(self.base+self.altura+((self.base ** 2 + self.altura**2)**(1/2)))
