from flask import Flask,render_template
import sqlite3
app = Flask(__name__)
#@app.route('/')
#def index():
#return render_template("main.html")

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
#INSERTAR DATOS
    #cursor.execute("INSERT INTO datos_estacion_02 VALUES (null, '06/04/2021', 4, 5, 9)")
    conexion.commit()
#LISTAR DATOS
    cursor.execute("SELECT temperatura_max FROM datos_estacion_02;")
    temperaturas_max = cursor.fetchall()
    var1= [f[0] for f in temperaturas_max]
    
    cursor.execute("SELECT fecha FROM datos_estacion_02;")
    fechas = cursor.fetchall()
    var2= [f[0] for f in fechas]
    
    
    #print(temperaturas_max,"   ", fechas)
    #Cerrar conexion a base de datos
    conexion.close()

    return(var1, var2)
@app.route('/')
def temp():
    etiqueta = based()
    temperaturas_max = etiqueta[0]
    fechas= etiqueta[1]
    weekle_temps = [("lun",12),("mart",2),("mierc",20),("jue",23),("vier",8),("sab",12),("dom",30)]
    labels = [row[0] for row in weekle_temps]
    values = [row[1] for row in weekle_temps]
    return render_template("index.html",labels =fechas, values=temperaturas_max)
