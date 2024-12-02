from Clases import *
print ("1. Cuadrado, 2. Triangulo, 3.Circulo")
Desafio=input() 
if Desafio==1:
	print ("Ingrese lado") 
	Lado=float(input())
	FiguraElegida=Cuadrado(Lado)
	print (f"El area del cuadrado es:{FiguraElegida.calcularArea()}")
	print(f"El perimetro es:{FiguraElgida.calcularPerimetro()}")