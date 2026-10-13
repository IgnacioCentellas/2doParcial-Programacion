import mysql.connector
from mysql.connector import Error
import datetime

DB_HOST = "localhost"
DB_USER = "Ignacio" 
DB_PASSWORD = "admin1234"
DB_NAME = "inventario_ropa"
ARCHIVO_LOG = "log_operaciones.txt"

def registrar_log(accion):
    try:
        with open(ARCHIVO_LOG, "a", encoding="utf-8") as archivo:
            fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            archivo.write(f"[{fecha_hora}] {accion}\n")
    except IOError as e:
        print(f"Error al escribir en el log: {e}")
