from typing import List, Optional


# Modelo de Cliente
class Cliente:
    def __init__(self, dni: str, nombre: str, apellido: str, direccion: str, telefono: str):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__telefono = telefono
    # Metodo de acceso al dni
    def get_dni(self):
        return self.__dni
    # Metodo de acceso al nombre

    def get_nombre(self):
        return self.__nombre
    # Metodo de acceso al apellido

    def get_apellido(self):
        return self.__apellido


    def __str__(self):
        return f"Cliente({self.__dni}, {self.__nombre} {self.__apellido}, {self.__direccion}, {self.__telefono})"


# Modelo de Contrato
class Contrato:
    def __init__(self, cliente: Cliente, plan: str, fecha_inicio: str, modem_serial: str, modem_modelo: str):
        self.__cliente = cliente
        self.__plan = plan
        self.__fecha_inicio = fecha_inicio
        self.__modem_serial = modem_serial
        self.__modem_modelo = modem_modelo

    def __str__(self):
        return (f"Contrato(Cliente: {self.__cliente.get_nombre()} {self.__cliente.get_apellido()}, Plan: {self.__plan}, "
                f"Fecha de inicio: {self.__fecha_inicio}, Modem: {self.__modem_serial} - {self.__modem_modelo})")


# DAO para Clientes
class ClienteDAO:
    def __init__(self):
        self.__clientes: List[Cliente] = []

    def agregar(self, cliente: Cliente) -> None:
        if any(c.get_dni() == cliente.get_dni() for c in self.__clientes):  # Cambio c.dni y cliente.dni por el metodo de acceso
            raise ValueError(f"Ya existe un cliente con DNI {cliente.dni}")
        self.__clientes.append(cliente)

    def obtener_por_dni(self, dni: str) -> Optional[Cliente]:
        for cliente in self.__clientes:
            if cliente.get_dni() == dni:  # Cambio cliente.dni por el metodo de acceso
                return cliente
        return None

    def listar_todos(self) -> List[Cliente]:
        return self.__clientes


# DAO para Contratos
class ContratoDAO:
    def __init__(self):
        self.__contratos: List[Contrato] = []

    def agregar(self, contrato: Contrato) -> None:
        self.__contratos.append(contrato)

    def listar_por_zona(self, zona: str) -> List[Contrato]:
        # Este método puede implementarse si se tiene una relación con zonas
        return self.__contratos  # Simulando que retorna todos por ahora
    
    # Metodo de acceso a los contratos
    def get_contratos(self):
        return self.__contratos


# Lógica de negocio
class GestorClientes:
    def __init__(self, cliente_dao: ClienteDAO, contrato_dao: ContratoDAO):
        self.__cliente_dao = cliente_dao
        self.__contrato_dao = contrato_dao

    def registrar_cliente(self, dni: str, nombre: str, apellido: str, direccion: str, telefono: str) -> Cliente:
        cliente = Cliente(dni, nombre, apellido, direccion, telefono)
        self.__cliente_dao.agregar(cliente)
        return cliente

    def buscar_cliente(self, dni: str) -> Optional[Cliente]:
        return self.__cliente_dao.obtener_por_dni(dni)

    def listar_clientes(self) -> List[Cliente]:
        return self.__cliente_dao.listar_todos()

    def generar_contrato(self, dni: str, plan: str, fecha_inicio: str, modem_serial: str, modem_modelo: str) -> Contrato:
        cliente = self.__cliente_dao.obtener_por_dni(dni)
        if not cliente:
            raise ValueError(f"No se encontró un cliente con DNI {dni}")
        contrato = Contrato(cliente, plan, fecha_inicio, modem_serial, modem_modelo)
        self.__contrato_dao.agregar(contrato)
        return contrato

def main():
    # Instancias de DAOs
    cliente_dao = ClienteDAO()
    contrato_dao = ContratoDAO()

    # Gestor
    gestor = GestorClientes(cliente_dao, contrato_dao)

    # Alta de clientes
    cliente1 = gestor.registrar_cliente("12345678", "María", "Pérez", "Calle 123", "123456789")
    cliente2 = gestor.registrar_cliente("87654321", "Juan", "López", "Avenida 456", "987654321")

    # Búsqueda de cliente
    buscado = gestor.buscar_cliente("12345678")
    print("Cliente encontrado:", buscado)

    # Listar todos los clientes
    print("\nLista de clientes:")
    for cliente in gestor.listar_clientes():
        print(cliente)

    # Generar contrato
    contrato1 = gestor.generar_contrato("12345678", "200Mb", "2024-12-01", "SN123456", "ModeloX")
    print("\nContrato generado:", contrato1)

    # Listar contratos (por ahora muestra todos)
    print("\nLista de contratos:")
    for contrato in contrato_dao.get_contratos():  # cambie por el metodo de acceso al los contratos dao
        print(contrato)



# Pruebas
if __name__ == "__main__":  # Movi el contenido del if a la funcion main()
    main()