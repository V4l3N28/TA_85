from flask import Flask, render_template, flash, request, redirect, url_for, jsonify, session, send_file, current_app, g
from db import get_db, close_db
from datetime import datetime
from flask_mysqldb import MySQLdb

app= Flask(__name__)

#conexion a la base de datos
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'bases'

mysql= MySQL(app)

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000, debug=True)

#este .py tiene la finalidad de mapear cada uno de los links con su respectiva funcion
#Conexion a \templates\HOME la cual seria establecida como la pagina principal
# este @app.route('/') siempre tiene que estar definido con un solo "/"
@app.route('/')
def HOME():
  return render_template("HOME.html")

##Conexion a \templates\ventanaInicioSESION


@app.route('/IniciarSesion/', methods=['GET', 'POST'])
def ventanaInicioSESION():
    if g.user:
        return redirect( url_for('vistaCrud' ))
    if request.method == 'POST':
      usuario = request.form['usuario']
      contrasena = request.form['contrasena']
      error = None
      db = get_db() #funcion que se conecta a la BD
      usuario = db.execute('SELECT * FROM usuarios WHERE usuario = ?', (usuario,)).fetchone()
      contrasena = db.execute('SELECT * FROM usuarios WHERE contrasena = ?', (contrasena,)).fetchone()
    if user is None:
      return 'Usuario o contraseña Incorrectos'
    else:
      if check_password_hash( usuario[5], contrasena):
        session.clear()
        session['user_id'] = user[0]
    return render_template("vistacrud.html")

    return render_template("ventanaInicioSESION.html")

##Conexion a \templates\entanvaRegistroUSUARIO
@app.route('/Registrarse/', methods=['GET', 'POST'])
def ventanaRegistroUSUARIO():
    if request.method == 'POST':
        
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        email2 = request.form['email']
        contrasena = request.form['contrasena']
        contrasena2 = request.form['contrasena']
        ususario = request.form['usuario']

        cursor=mysql.connection.cursor()
        cursor.execute("INSERT INTO usuarios VALUES(NULL, %s, %s, %s, %s, %s, %s, %s"), (nombre, apellido, email, contrasena, ususario)
        cursor.conection.commit()

        return redirect(url_for('HOME'))
  
    return render_template("ventanaRegistroUSUARIO.html")

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
  return render_template("PRONOSTICOS.html")

##Conexion a \templates\GENERAL
@app.route('/General/')
def GENERAL():
  return render_template("GENERAL.html")

##Conexion a \templates\ESTACIONES
@app.route('/Estaciones/')
def ESTACIONES():
  return render_template("ESTACIONES.html")
