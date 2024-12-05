#from clases import Figuras
from clases import *
print ("1. Cuadrado, 2. Triangulo, 3.Rectangulo, 4.Circulo")
Desafio=int(input() )
if Desafio==1:
	print ("Ingrese lado") 
	Lado=float(input())
	FiguraElegida=Cuadrado(Lado)
	print (f"El area del cuadrado es:{FiguraElegida.calcularArea()}")
	print(f"El perimetro es:{FiguraElegida.calcularPerimetro()}")
if Desafio==2:
	print ("Ingrese base") 
	Lado=float(input())
	print ("Ingrese altura") 
	altura=float(input())
	FiguraElegida=Triangulo(Lado,altura)
	print (f"El area   es:{FiguraElegida.calcularArea()}")
	print(f"El perimetro es:{FiguraElegida.calcularPerimetro()}")
if Desafio==3:
	print ("Ingrese base") 
	Lado=float(input())
	print ("Ingrese altura") 
	altura=float(input())
	FiguraElegida=Rectangulo(Lado,altura)
	print (f"El area   es:{FiguraElegida.calcularArea()}")
	print(f"El perimetro es:{FiguraElegida.calcularPerimetro()}")
if Desafio==4:
	print ("Ingrese radio") 
	radio=float(input())
	FiguraElegida=Circulo(radio)
	print (f"El area   es:{FiguraElegida.calcularArea()}")
	print(f"El perimetro es:{FiguraElegida.calcularPerimetro()}")