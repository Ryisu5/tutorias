import Producto 



def registrarProducto():
	Nombre=input("Ingrese Nombre")
	Precio=float(input("Ingrese Precio"))
	return Producto(Nombre, Precio)
Encendido=True 
while Encendido:
	print("Opciones:")
	print ("1. registrar Producto")
	print ("2. Actualizar Stock")
	print ("3. Calcular inventario")
	print ("4. Ver datos del producto")
	print ("5. Salir")
	opcion=input("seleccione una opcion (1-5)")
	if opcion=="1":
		Producto1=registrarProducto()
	elif opcion =="2":
		cantidad =int(input("Ingrese la cantidad agregar (positiva) o restar (negativa):"))
		Producto1.actualizarStock(cantidad)
	elif opcion=="3":
		print (f"El total del inventario es: {Producto1.calcularinventario()}")
	elif opcion=="4":
		datos=Producto1.verdatos()
		print(datos)
	elif opcion=="5":
		print ("Saliendo de la aplicacion")
		break
	else: 
		print ("Opcion no valida. Intente de nuevo")
