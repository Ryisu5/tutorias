import sqlite3  

class Database:  
    def __init__(self, db_name='telered.db'):  
        self.conn = sqlite3.connect(db_name)  
        self.create_tables()  

    def create_tables(self):  
        cursor = self.conn.cursor()  
        cursor.execute('''  
            CREATE TABLE IF NOT EXISTS clientes (  
                id INTEGER PRIMARY KEY AUTOINCREMENT,  
                dni TEXT UNIQUE NOT NULL,  
                nombre TEXT NOT NULL,  
                apellido TEXT NOT NULL,  
                direccion TEXT NOT NULL,  
                telefono TEXT NOT NULL  
            )  
        ''')  
        cursor.execute('''  
            CREATE TABLE IF NOT EXISTS servicios (  
                id INTEGER PRIMARY KEY AUTOINCREMENT,  
                client_id INTEGER,  
                plan TEXT NOT NULL,  
                fecha_inicio TEXT,  
                FOREIGN KEY(client_id) REFERENCES clientes(id)  
            )  
        ''')  
        cursor.execute('''  
            CREATE TABLE IF NOT EXISTS dispositivos (  
                id INTEGER PRIMARY KEY AUTOINCREMENT,  
                service_id INTEGER,  
                numero_serie TEXT UNIQUE NOT NULL,  
                modelo TEXT NOT NULL,  
                FOREIGN KEY(service_id) REFERENCES servicios(id)  
            )  
        ''')  
        self.conn.commit()  

    def close(self):  
        self.conn.close()  


class Cliente:  
    def __init__(self, dni, nombre, apellido, direccion, telefono):  
        self.dni = dni  
        self.nombre = nombre  
        self.apellido = apellido  
        self.direccion = direccion  
        self.telefono = telefono  

    def guardar(self, db):  
        cursor = db.conn.cursor()  
        cursor.execute('''  
            INSERT INTO clientes (dni, nombre, apellido, direccion, telefono)  
            VALUES (?, ?, ?, ?, ?)  
        ''', (self.dni, self.nombre, self.apellido, self.direccion, self.telefono))  
        db.conn.commit()  


class GestorClientes:  
    def __init__(self, db):  
        self.db = db  

    def alta_cliente(self, dni, nombre, apellido, direccion, telefono):  
        cliente = Cliente(dni, nombre, apellido, direccion, telefono)  
        try:  
            cliente.guardar(self.db)  
            print(f"Cliente {nombre} {apellido} agregado exitosamente.")  
        except sqlite3.IntegrityError:  
            print(f"Error: El DNI {dni} ya está registrado.")  

    def buscar_cliente(self, dni):  
        cursor = self.db.conn.cursor()  
        cursor.execute('SELECT * FROM clientes WHERE dni = ?', (dni,))  
        cliente = cursor.fetchone()  
        return cliente  