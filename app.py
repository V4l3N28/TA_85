#Importar el módulo de flask en el proyecto es obligatorio. Un objeto de la clase Flask es nuestra aplicación WSGI.
from flask import Flask, render_template, url_for, current_app, g, request, redirect, session
import sqlite3
import functools
import pandas as pd
import numpy as np
import matplotlib.pyplot  as plt


app = Flask(
  __name__,
  template_folder='templates')


#Se define una funcion get_db() en donde se utiliza un bloque try except el cual captura un error en el caso de que suceda
#Dentro de try abrimos un condicional if en donde verificamos si una variable 'db' no está en g (variables globales)
# si 'db' no está en g, entonces nos conectamos a la base de datos y le asignamos db a las variables globales
def get_db():
    try:
        if 'db' not in g:
            g.db = sqlite3.connect('bases_04.db')
        return g.db
    except Error:
        print(Error)

#Se define una funcion close_db() en donde borramos db de las variables globales y verificamos si esa variable fue borrada
#Luego cerramos la base de datos
def close_db():
    db = g.pop( 'db', None )

    if db is not None:
        db.close()


#Se define una funcion load_logged_in_user() en la cual se obtiene un user_id de la sesion y se guarda en una variable para trabajarlo más comodamente
#Si el usuario de la sesion (user_id) está vacío, se le asigna a None a la variable global de user
#En el caso contrario, si el usuario de la sesión no está vacío, se obtiene ese dato de la base de datos y se le asigna la variable global
@app.before_request
def load_logged_in_user():
    user_id = session.get( 'user_id' )

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM usuarios WHERE id = ?', (user_id,)
        ).fetchone()


#Se hace la conexión a la base de datos bases_07.db por medio de la asignación a una variable conn
conn=sqlite3.connect('bases_04.db')
#Se crea un cursor 
cursor = conn.cursor()

#Dentro de la conexion se convierten las tablas importadas de la hoja tablas.py a tablas de sql
#veredas.to_sql('veredas', conn)
#observadores.to_sql('dfo', conn)
#fincas.to_sql('fincas', conn)
#registros.to_sql('registros', conn)
#usuarios.to_sql('usuarios', conn)

#En este punto, se corre el programa para la creación de la base de datos y se comentan las líneas de creación de tablas (debido a que si se dejan, el programa lanzará un mensaje diciendo que las tablas ya fueron creadas anteriormente)
#Se define una variable df como el Dataframe del contenido de la variable cursor y se define el nombre de sus columnas
df = pd.DataFrame(cursor, columns=['fecha','precipitacion','temperaturaMaxima','temperaturaMinima'])

#Se procede a la creacion de varias funciones como sumatoria, promedio, valor máximo y valor mínimo del filtro de datos en columnas específicas, cada funcion pide  dos cosas; un año y un dataframe
def sumatoria_prec(year,df):
    #En la línea 31 se utiliza la siguiente estructura (línea 27) para obtener la sumatoria de la precipitacion por mes de un año en específico
    #cursor.execute("SELECT strftime('%m', date) as valmonth, SUM(column) FROM registros WHERE strftime('%Y', date)='year_number' GROUP BY valmonth")
    #En la estructura anterior se hace una seleccion (por medio de un SELECT) de los meses dentro de una columna (asignandole un nombre por medio de 'as' un nombre 'month') y de la sumatoria de otra columna(por medio de la funcion SUM()) 
    #Estos datos se recolectan de una tabla de datos (por medio de FROM) y se utiliza un filtro de datos (WHERE) en el que se pide que esos datos estén dentro de un valor de año dado por la variable year. 
    #Además, se agrupan estos datos por meses (por medio de GROUP BY month).
    cursor.execute("SELECT strftime('%m', fecha) as month, SUM(precipitacion) FROM registros WHERE strftime('%Y', fecha)=? GROUP BY month",[year])
    #Por medio de un fetchall() se recolectan los datos filtrados del cursor
    filtered_db= cursor.fetchall()
    #Estos datos se convierten a Dataframe con nombre de columnas especificados
    db_to_dataframe= pd.DataFrame(filtered_db,columns=['fecha','precipitacion'])
    #Se retorna el dataframe
    return db_to_dataframe

#En las siguientes definiciones se aplica la misma estructura de la funcion sumatoria exceptuando que no se pide un resultado por meses sino que solo se pide un solo valor
#(No se utiliza GROUP BY month para que la funcion solo nos arroje un resultado general y no por partes)
def promedio_prec(year,df):
    cursor.execute("SELECT strftime('%m', fecha) as month, AVG(precipitacion) FROM registros WHERE strftime('%Y', fecha)=?",[year])
    filtered_db= cursor.fetchall()
    db_to_dataframe= pd.DataFrame(filtered_db,columns=['fecha','precipitacion'])
    return db_to_dataframe

def temp_max(year,df):
    cursor.execute("SELECT strftime('%m', fecha) as month, MAX(temperaturaMaxima) FROM registros WHERE strftime('%Y', fecha)=?",[year])
    filtered_db= cursor.fetchall()
    db_to_dataframe= pd.DataFrame(filtered_db,columns=['fecha','temperaturaMaxima'])
    return db_to_dataframe

def temp_min(year,df):
    cursor.execute("SELECT strftime('%m', fecha) as month, MIN(temperaturaMinima) FROM registros WHERE strftime('%Y', fecha)=?",[year])
    filtered_db= cursor.fetchall()
    db_to_dataframe= pd.DataFrame(filtered_db,columns=['fecha','temperaturaMinima'])
    return db_to_dataframe




#este .py tiene la finalidad de mapear cada uno de los links con su respectiva funcion
#Conexion a \templates\HOME la cual seria establecida como la pagina principal
# este @app.route('/') siempre tiene que estar definido con un solo "/"

'''app.route(rule, options)
    El parámetro de regla (rule) representa el enlace de URL con la función.
    Las opciones (options) son una lista de parámetros que se enviarán al objeto Regla subyacente.'''
@app.route('/')
def HOME():
  return render_template("HOME.html")

##Conexion a \templates\ventanaInicioSESION
@app.route('/IniciarSesion/', methods=('GET','POST'))
def iniciosesion():
  return render_template("ventanaInicioSESION.html")

##Conexion a \templates\entanvaRegistroUSUARIO
@app.route('/Registrarse/', methods=('GET','POST'))
#Se define una función ventanaRegistroUSUARIO(), la cual verifica si el usuario ya está registrado y lo envía al home
#Se abre un bloque try except en donde se toman los datos del formulario (request.form), se verifica que el correo y las contraseñas sean iguales
# Y se insertan esos valores en la base de datos, si los correos y contraseñas no son iguales se redirige a la ventana de registro de usuario
def ventanaRegistroUSUARIO():
  if g.user:
    return redirect( url_for( '/' ) )
  try:
    if request.method == 'POST':
      nombre = request.form['nombre']
      apellido = request.form['apellido']
      usuario = request.form['usuario']
      correo = request.form['email']
      correo2 = request.form['email2']
      contrasena = request.form['contrasena']
      contrasena2 = request.form['contrasena2']
      if correo == correo2 and contrasena == contrasena2:
        db = get_db()
        db.execute("INSERT INTO usuarios(nombre, apellido, usuario, email, contrasena) VALUES ('%s','%s','%s','%s','%s')" % (nombre, apellido, usuario, correo, contrasena))
        db.commit()
        return render_template('ventanaInicioSESION.html')
      else:
        return render_template("ventanaRegistroUSUARIO.html", nombre = nombre, Apellido = apellido, Usuario=usuario)
    return render_template("ventanaRegistroUSUARIO.html")
  except:
    return "Este correo o usuario ya está registrado."

##Conexion a \templates\CambiarCLAVE
@app.route('/ChangePassword/')
def CambiarCLAVE():
  return render_template("CambiarCLAVE.html")

##Conexion a \templates\RecuperarCLAVE
@app.route('/RecuperarClave/')
def RecuperarCLAVE():
  return render_template("RecuperarCLAVE.html")

##Conexion a \templates\PRONOSTICOS
@app.route('/Pronosticos/')
def PRONOSTICOS():
  precipitacion=[("lluvias por encima de lo normal",50),("lluvias dentro de lo normal",16),("lluvias poor debajo de lo normal",10)]
  labels = [item[0] for item in precipitacion]
  values = [row[1] for row in precipitacion]
  return render_template("PRONOSTICOS.html",labels= labels,values=values)

##Conexion a \templates\GENERAL
@app.route('/General/')
def GENERAL():
  if g.user is None:
    return redirect( url_for( 'iniciosesion' ) ) 
  else:    
    temperaturaMinima=[("enero",12,13,24,10,17,21,32),("febrero",14,12,22,10,19,28,30),("marzo",14,23,24,11,17,21,31),("abril",10,19,27,10,16,21,35)]
    labels1 = [item[0] for item in temperaturaMinima]
    value1 = [row[1] for row in temperaturaMinima]
    value2 = [row[2] for row in temperaturaMinima]
    value3 = [row[3] for row in temperaturaMinima]
    value4 = [row[4] for row in temperaturaMinima]
    value5 = [row[5] for row in temperaturaMinima]
    value6 = [row[6] for row in temperaturaMinima]
    value7 = [row[7] for row in temperaturaMinima]
    
    temperaturaMaxima=[("productor1",14),("productor2",25),("productor3",37)]
    labels2 = [item[0] for item in temperaturaMaxima]
    values = [row[1] for row in temperaturaMaxima]
    return render_template("GENERAL.html",labels1= labels1,labels2= labels2,values=values, value1=value1,value2=value2,value3=value3,value4=value4,value5=value5,value6=value6,value7=value7)

##Conexion a \templates\ESTACIONES
@app.route('/Estaciones/')
def ESTACIONES():
  temperaturaMaxima=[("productor1",34),("productor2",56),("productor3",17)]
  labels = [item[0] for item in temperaturaMaxima]
  values = [row[1] for row in temperaturaMaxima]
  return render_template("ESTACIONES.html",labels= labels,values=values)


#El constructor de  toma el nombre del módulo actual (__name__) como argumento.
if __name__ == "__main__":
      #El método run () de la clase Flask ejecuta la aplicación en el servidor de desarrollo local.
  #app.run(host, port, debug, options) - todos los parametros son opcionales

  ''' host (anfitrion) - El valor predeterminado es 127.0.0.1 (localhost). Configure en "0.0.0.0" para que el servidor esté disponible externamente
      port(puerto) - El valor predeterminado es 5000
      debug - El valor predeterminado es falso. Si se establece en verdadero, proporciona información del debug.
      options(opciones) - Para ser reenviado al servidor de herramientas subyacente.'''
  
  app.run( host='0.0.0.0', debug=True, port=8080)
  