import unittest  
import os  

class TestGestorClientes(unittest.TestCase):  
    @classmethod  
    def setUpClass(cls):  
        cls.db = Database(':memory:')  # Usar una base de datos en memoria para pruebas  
        cls.gestor = GestorClientes(cls.db)  

    def test_alta_cliente(self):  
        self.gestor.alta_cliente('12345678', 'Juan', 'Pérez', 'Calle Ejemplo 1', '123456789')  
        cliente = self.gestor.buscar_cliente('12345678')  
        self.assertIsNotNone(cliente)  
        self.assertEqual(cliente[1], 'Juan')  

    def test_alta_cliente_repetido(self):  
        self.gestor.alta_cliente('12345678', 'Maria', 'Gomez', 'Calle Falsa 123', '987654321')  
        cliente = self.gestor.buscar_cliente('12345678')  
        self.assertEqual(cliente[2], 'Juan')  # El cliente no debería haberse agregado  

if __name__ == '__main__':  
    unittest.main()  