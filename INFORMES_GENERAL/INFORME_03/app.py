from flask import Flask, render_template

app= Flask(__name__)

##Conexion a \templates\HOME
@app.route('/Inicio/')
def HOME():
return render_template("HOME.html")

##Conexion a \templates\ventanaRegistroSESION
@app.route('/IniciarSesion/')
def ventanaRegistroSESION():
return render_template("ventanaRegistroSESION.html")

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
