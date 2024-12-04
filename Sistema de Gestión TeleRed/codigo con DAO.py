from typing import List, Optional


# Modelo de Cliente
class Cliente:
    def __init__(self, dni: str, nombre: str, apellido: str, direccion: str, telefono: str):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Cliente({self.dni}, {self.nombre} {self.apellido}, {self.direccion}, {self.telefono})"


# Modelo de Contrato
class Contrato:
    def __init__(self, cliente: Cliente, plan: str, fecha_inicio: str, modem_serial: str, modem_modelo: str):
        self.cliente = cliente
        self.plan = plan
        self.fecha_inicio = fecha_inicio
        self.modem_serial = modem_serial
        self.modem_modelo = modem_modelo

    def __str__(self):
        return (f"Contrato(Cliente: {self.cliente.nombre} {self.cliente.apellido}, Plan: {self.plan}, "
                f"Fecha de inicio: {self.fecha_inicio}, Modem: {self.modem_serial} - {self.modem_modelo})")


# DAO para Clientes
class ClienteDAO:
    def __init__(self):
        self.clientes: List[Cliente] = []

    def agregar(self, cliente: Cliente) -> None:
        if any(c.dni == cliente.dni for c in self.clientes):
            raise ValueError(f"Ya existe un cliente con DNI {cliente.dni}")
        self.clientes.append(cliente)

    def obtener_por_dni(self, dni: str) -> Optional[Cliente]:
        for cliente in self.clientes:
            if cliente.dni == dni:
                return cliente
        return None

    def listar_todos(self) -> List[Cliente]:
        return self.clientes


# DAO para Contratos
class ContratoDAO:
    def __init__(self):
        self.contratos: List[Contrato] = []

    def agregar(self, contrato: Contrato) -> None:
        self.contratos.append(contrato)

    def listar_por_zona(self, zona: str) -> List[Contrato]:
        # Este método puede implementarse si se tiene una relación con zonas
        return self.contratos  # Simulando que retorna todos por ahora


# Lógica de negocio
class GestorClientes:
    def __init__(self, cliente_dao: ClienteDAO, contrato_dao: ContratoDAO):
        self.cliente_dao = cliente_dao
        self.contrato_dao = contrato_dao

    def registrar_cliente(self, dni: str, nombre: str, apellido: str, direccion: str, telefono: str) -> Cliente:
        cliente = Cliente(dni, nombre, apellido, direccion, telefono)
        self.cliente_dao.agregar(cliente)
        return cliente

    def buscar_cliente(self, dni: str) -> Optional[Cliente]:
        return self.cliente_dao.obtener_por_dni(dni)

    def listar_clientes(self) -> List[Cliente]:
        return self.cliente_dao.listar_todos()

    def generar_contrato(self, dni: str, plan: str, fecha_inicio: str, modem_serial: str, modem_modelo: str) -> Contrato:
        cliente = self.cliente_dao.obtener_por_dni(dni)
        if not cliente:
            raise ValueError(f"No se encontró un cliente con DNI {dni}")
        contrato = Contrato(cliente, plan, fecha_inicio, modem_serial, modem_modelo)
        self.contrato_dao.agregar(contrato)
        return contrato


# Pruebas
if __name__ == "__main__":
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
    for contrato in contrato_dao.contratos:
        print(contrato)