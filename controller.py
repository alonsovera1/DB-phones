#Insertar registro en una tabla
import sqlite3

#Realizar conexion
def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)

        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexion:',error)

#def crear_tabla(conexion, definicion):
#	cursor = conexion.cursor()
#	cursor.execute(definicion)
#	conexion.commit()

def mostrar_tablas(conexion):
	sql = "SELECT name FROM sqlite_master WHERE type='table';"

	cursor = conexion.cursor()
	cursor.execute(sql)
	tablas = cursor.fetchall()

	for t in tablas:
		print(t[0])

def crear_usuario(conexion, usuario):
	sql = 'INSERT INTO usuario VALUES (?, ?, ?);'

	cursor = conexion.cursor()
	cursor.execute(sql, usuario)

	conexion.commit()

conexion = crear_conexion('registro.db')

#Admision de tablas
sql = """
CREATE TABLE usuario (
	id INTEGER NOT NULL,
	nombre TEXT NOT NULL,
	clave TEXT NOT NULL
);
"""
#crear_tabla(conexion, sql)

#Ingresar datos - usuario
while True:
	try:
		id_usuario = int(input('Ingrese el ID del usuario: '))

		if id_usuario > 0:
			break
		else:
			print('Debe ingresar un valor entero positivo.')
	except ValueError:
		print('Debe ingresar un valor entero')

	print()


while True:
	nombre = input('Ingrese un nombre: ').strip()

	if len(nombre):
		break
	else:
		print('Debe ingresar una cadena con un valor especifico para el nombre.')

		print()


while True:
	clave = input('Ingrese su clave: ').strip()

	if len(clave):
		break
	else:
		print('Debe ingresar una cadena con un valor especifico para la clave.')

		print()

crear_usuario(conexion, (id_usuario, nombre, clave))

if conexion:
	conexion.close()