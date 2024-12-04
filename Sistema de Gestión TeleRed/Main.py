def main():  
    db = Database()  
    gestor = GestorClientes(db)  

    while True:  
        print("\n1. Alta de cliente\n2. Buscar cliente\n3. Salir")  
        opcion = input("Selecciona una opción: ")  

        if opcion == '1':  
            dni = input("Ingrese DNI: ")  
            nombre = input("Ingrese nombre: ")  
            apellido = input("Ingrese apellido: ")  
            direccion = input("Ingrese dirección: ")  
            telefono = input("Ingrese teléfono: ")  
            gestor.alta_cliente(dni, nombre, apellido, direccion, telefono)  

        elif opcion == '2':  
            dni = input("Ingrese DNI del cliente a buscar: ")  
            cliente = gestor.buscar_cliente(dni)  
            if cliente:  
                print("Cliente encontrado:", cliente)  
            else:  
                print("Cliente no encontrado.")  

        elif opcion == '3':  
            break  

    db.close()  

if __name__ == "__main__":  
    main()  