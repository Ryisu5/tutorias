import requests
import json
import random
import time
# URL del servidor Flask y la ruta de la API
url = "http://192.168.0.4:5000/insertar"
def loop():
	
	while True:
	# Datos que queremos enviar (temperatura y humedad)
		
		data = {
		    'valor': random.randint(-20, 100),
		}

		# Enviar la solicitud POST con los datos como JSON
		response = requests.post(url, json=data)

		# Verificar la respuesta del servidor
		if response.status_code == 200:
		    print("Datos enviados correctamente.")
		    print(f"Respuesta del servidor: {response.json()}")
		else:
		    print(f"Error al enviar datos: {response.status_code}")
		time.sleep(5)
if __name__ == '__main__':
    loop()
