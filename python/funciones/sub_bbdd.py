from funciones.menu import *
from funciones.sub_grafana import *
import mysql.connector,time


# Función para ejecutar consultas en el mismo segundo
def execute_queries():
    # Configura la conexión con el servidor MariaDB
    config = {
        'user': 'user',
        'password': 'clave',
        'host': '127.0.0.1',
        'database': 'drupal'
    }
    connection = mysql.connector.connect(**config)

    # Pide el número de consultas a ejecutar
    num_queries = int(input("Ingrese el número de consultas a ejecutar: "))

    # Ejecuta las consultas
    times = []
    for i in range(num_queries):
        start_time = time.time()
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchall()
        end_time = time.time()
        times.append(end_time - start_time)

    # Imprime los resultados
    print(f"Se ejecutaron {num_queries} consultas.")
    print(f"Tiempo total de ejecución: {sum(times)} segundos")
    print(f"Tiempo promedio de ejecución por consulta: {sum(times) / num_queries} segundos")
    print()

    # Cierra la conexión con el servidor MariaDB
    connection.close()
