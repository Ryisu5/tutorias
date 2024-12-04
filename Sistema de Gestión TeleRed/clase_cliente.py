from typing import List, Optional

class Cliente:
    def __init__(self, dni: str, nombre: str, apellido: str, direccion: str, telefono: str):
    	# Posible correccion es el poner los atributos en privado ya que el enenciadte pide encapsulaminento
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__telefono = telefono
    # Te agrego el metodo de acceso a dni ya que al poner los atributos en privado es necesario el metodo de acceso
    def get_dni(self):
    	return self.__dni
    def __str__(self):
        return f"Cliente({self.__dni}, {self.__nombre} {self.__apellido}, {self.__direccion}, {self.__telefono})"



