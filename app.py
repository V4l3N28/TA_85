from flask import Flask, render_template, url_for
from conexion import based

app= Flask(__name__)

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000, debug=True)

#este .py tiene la finalidad de mapear cada uno de los links con su respectiva funcion
#Conexion a \templates\HOME la cual seria establecida como la pagina principal
# este @app.route('/') siempre tiene que estar definido con un solo "/"
@app.route('/')
def HOME():
  return render_template("HOME.html")

##Conexion a \templates\ventanaInicioSESION
@app.route('/IniciarSesion/')
def ventanaInicioSESION():
  return render_template("ventanaInicioSESION.html")

##Conexion a \templates\entanvaRegistroUSUARIO
@app.route('/Registrarse/')
def ventanaRegistroUSUARIO():
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