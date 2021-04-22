from flask import Flask,render_template
import sqlite3
app = Flask(__name__)
#@app.route('/')
#def index():
#   return render_template("main.html")

def based():
    #Conexión a base de datos
    conexion= sqlite3.connect('basedatos.db')
