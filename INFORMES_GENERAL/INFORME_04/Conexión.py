from flask import Flask,render_template
import sqlite3
app = Flask(__name__)
#@app.route('/')
#def index():
#   return render_template("main.html")

def based():
    #Conexión a base de datos
    conexion= sqlite3.connect('basedatos.db')
  #Crear cursor
    cursor = conexion.cursor()
    #Crear tabla
    cursor.execute("CREATE TABLE IF NOT EXISTS datos_estacion_02("+
    "id INTEGER PRIMARY KEY AUTOINCREMENT, "+
    "fecha DATE, "+
    "temperatura_min INTEGER, "+
    "temperatura_max INTEGER, "+
    "lluvias INTEGER"+
    ")")
  #GUARDAR CAMBIOS
    conexion.commit()
