from flask import Flask,render_template
import sqlite3
app = Flask(__name__)


def based():
    #estamos conectando una base de datos SQLite3 a python mediante el comando sqlite3.connect('')
    #Conexión a base de datos
    conexion= sqlite3.connect('basedatos.db')

    #Crear cursor
    cursor = conexion.cursor()
    #Para crear una tabla de nombre "name" se usa el comando  .execute("CREATE TABLE name
	#se usara el comando .execute("CREATE TABLE IF NOT EXISTS name para que cree una taba si no hay existencia de ella en una base de datos
    #Se crearan 4 tablas con los nombres fincas, observadores,registros y veredas
	cursor.execute("CREATE TABLE IF NOT EXISTS fincas("+
	"id	INTEGER PRIMARY KEY AUTOINCREMENT, "+
	"idArea	INTEGER NOT NULL FOREIGN KEY REFERENCES veredas(id),"+
	"finca	INTEGER NOT NULL,"+
	")")

    cursor.execute("CREATE TABLE IF NOT EXISTS observadores ("+
	"id	INTEGER PRIMARY KEY AUTOINCREMENT,"+
	"primerNombre	TEXT NOT NULL,"+
	"segundoNombre	TEXT,"+
	"apellidos	TEXT NOT NULL,"+
	"celular	INTEGER,"+
	"latitud	NUMERIC,"+
	"longitud	NUMERIC,"+
	")")

    cursor.execute("CREATE TABLE IF NOT EXISTS registros ("+
	"id	INTEGER PRIMARY KEY AUTOINCREMENT,"+
	"idFinca	INTEGER NOT NULL,"+
	"fecha	TEXT,"+
	"precipitacion	REAL,"+
	"temperaturaMaxima	REAL,"+
	"temperaturaMinima	REAL,"+
	")")
	
    cursor.execute("CREATE TABLE IF NOT EXISTS veredas ("+
	"id	INTEGER PRIMARY KEY AUTOINCREMENT,"+
	"departamento	TEXT NOT NULL,"+
	"ciudad	TEXT NOT NULL,"+
	"vereda	TEXT NOT NULL,"+
	")")

    conexion.commit() 
