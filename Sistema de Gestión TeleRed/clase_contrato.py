from typing import List, Optional
class Contrato:
    def __init__(self, cliente: Cliente, plan: str, fecha_inicio: str, modem_serial: str, modem_modelo: str):
    	# Posible correccion es el poner los atributos en privado ya que el enenciadte pide encapsulaminento
        
        self.__cliente = cliente
        self.__plan = plan
        self.__fecha_inicio = fecha_inicio
        self.__modem_serial = modem_serial
        self.__modem_modelo = modem_modelo

    def __str__(self):
        return (f"Contrato(Cliente: {self.__cliente.nombre} {self.__cliente.apellido}, Plan: {self.__plan}, "
                f"Fecha de inicio: {self.__fecha_inicio}, Modem: {self.__modem_serial} - {self.__modem_modelo})")