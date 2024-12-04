from CuentaBancaria import CuentaBancaria
def main():  # definiendo una funcion main
	numerocuenta=input ("Ingrese el numero de cuenta:")
	nombre=input("Ingrese su nombre:")
	apellido=input ("Ingrese su apellido:")

	cuenta=CuentaBancaria(numerocuenta,nombre, apellido)

	while True:
		print("opciones")
		print ("1. Depositar")
		print("2. Retirar")
		print("3. Ver saldo")
		print ("4. Salir")

		opcion=input("Seleccione una opcion (1-4):")

		if opcion=="1":
			cantidad=int(input("Ingrese la cantidad a depositar:"))
			cuenta.depositar(cantidad)
		elif opcion=="2":
			cantidad=int(input("Ingrese a cantidad a retirar:"))
			cuenta.retirar(cantidad)
		elif opcion=="3":
			cuenta.versaldo()
		elif opcion=="4":
			print ("Saliendo...")
			break
		else:
			print("Opcion no valida.Intente de nuevo")

if __name__ == "__main__":
	main()