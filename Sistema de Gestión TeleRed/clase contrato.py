from typing import List, Optional
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