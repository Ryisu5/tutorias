from typing import List, Optional
class GestorClientes:
    def __init__(self):
        self.clientes: List[Cliente] = []

    def alta_cliente(self, dni: str, nombre: str, apellido: str, direccion: str, telefono: str) -> Cliente:
        if any(c.dni == dni for c in self.clientes):
            raise ValueError(f"Ya existe un cliente con DNI {dni}")
        nuevo_cliente = Cliente(dni, nombre, apellido, direccion, telefono)
        self.clientes.append(nuevo_cliente)
        return nuevo_cliente

    def buscar_cliente(self, dni: str) -> Optional[Cliente]:
        for cliente in self.clientes:
            if cliente.dni == dni:
                return cliente
        return None

    def listar_clientes(self):
        return self.clientes


# Ejemplo de prueba
if __name__ == "__main__":
    gestor = GestorClientes()

    # Alta de clientes
    cliente1 = gestor.alta_cliente("12345678", "María", "Pérez", "Calle 123", "123456789")
    cliente2 = gestor.alta_cliente("87654321", "Juan", "López", "Avenida 456", "987654321")

    # Búsqueda de cliente
    buscado = gestor.buscar_cliente("12345678")
    print("Cliente encontrado:", buscado)

    # Listar todos los clientes
    print("\nLista de clientes:")
    for cliente in gestor.listar_clientes():
        print(cliente)

    # Ejemplo de error (DNI duplicado)
    try:
        gestor.alta_cliente("12345678", "Carlos", "Gómez", "Calle 789", "555555555")
    except ValueError as e:
        print("\nError:", e)