from typing import List, Optional

class Cliente:
    def __init__(self, dni: str, nombre: str, apellido: str, direccion: str, telefono: str):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Cliente({self.dni}, {self.nombre} {self.apellido}, {self.direccion}, {self.telefono})"



