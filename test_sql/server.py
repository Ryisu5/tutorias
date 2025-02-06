from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos MySQL
db_config = {
    'host': 'localhost',  # O la dirección IP de tu servidor de base de datos
    'user': 'root',
    'password': '',  # Cambia con la contraseña de tu base de datos
    'database': 'sensores'
}

# Conexión a la base de datos
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

# Ruta para insertar datos
@app.route('/insertar', methods=['POST'])
def insertar_dato():
    data = request.get_json()
    valor = data.get('valor')

    if valor is None:
        return jsonify({"error": "Falta el valor en la solicitud"}), 400

    try:
        # Conectar a la base de datos
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insertar el valor en la base de datos
        cursor.execute('INSERT INTO datos_sensor (valor) VALUES (%s)', (valor,))
        conn.commit()

        # Cerrar la conexión
        cursor.close()
        conn.close()

        return jsonify({"message": "Datos insertados correctamente"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Iniciar el servidor
if __name__ == '__main__':
    app.run(debug=True, host='192.168.0.4', port=5000)
