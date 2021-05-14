#Importar el módulo de flask en el proyecto es obligatorio. Un objeto de la clase Flask es nuestra aplicación WSGI.
from flask import Flask, render_template, url_for, current_app, g, request, redirect, session
from conexion import based
from defi import get_db, close_db, login_required

#El constructor de  toma el nombre del módulo actual (__name__) como argumento.
app= Flask(__name__)

  based()
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
  return render_template("PRONOSTICOS.html")

##Conexion a \templates\GENERAL
@app.route('/General/')
def GENERAL():
  return render_template("GENERAL.html")

##Conexion a \templates\ESTACIONES
@app.route('/Estaciones/')
def ESTACIONES():
  return render_template("ESTACIONES.html")

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

if __name__ == "__main__":
      #El método run () de la clase Flask ejecuta la aplicación en el servidor de desarrollo local.
  #app.run(host, port, debug, options) - todos los parametros son opcionales

  ''' host (anfitrion) - El valor predeterminado es 127.0.0.1 (localhost). Configure en "0.0.0.0" para que el servidor esté disponible externamente
      port(puerto) - El valor predeterminado es 5000
      debug - El valor predeterminado es falso. Si se establece en verdadero, proporciona información del debug.
      options(opciones) - Para ser reenviado al servidor de herramientas subyacente.'''
  
  app.run(host='127.0.0.1',port=5000, debug=True)