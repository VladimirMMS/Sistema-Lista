import psycopg2

conexion = psycopg2.connect(host="localhost",database="list_system", user="postgres", password="20012020")
cur = conexion.cursor()

