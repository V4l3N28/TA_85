#Importar el módulo de flask en el proyecto es obligatorio. Un objeto de la clase Flask es nuestra aplicación WSGI.
from flask import Flask, flash,render_template, url_for, current_app, g, request, redirect, session
import os,functools
from functools import wraps
import pandas as pd
import numpy as np
import random
import pyrebase


app = Flask(
  __name__,
  template_folder='templates')
app.secret_key = os.urandom( 24 )

#CONEXION BASE DATOS
firebaseConfig = {  
  "apiKey": "AIzaSyAvHOAhYaQN5B_1fgeTwCahxXlfy_DbqJM",
  "authDomain": "tesacdb-51ebe.firebaseapp.com",
  "databaseURL": "https://tesacdb-51ebe-default-rtdb.firebaseio.com",
  "projectId": "tesacdb-51ebe",
  "storageBucket": "tesacdb-51ebe.appspot.com",
  "messagingSenderId": "681673063098",
  "appId": "1:681673063098:web:57785e1179130ceed2a083"}


firebase = pyrebase.initialize_app(firebaseConfig)
def database():
    db = firebase.database()
    estaciones=db.child("ESTACIONES").get()
    data = pd.DataFrame(estaciones.val())
    return data



#push data
def insert(name,lastname,user,mail,password):
  db = firebase.database()
  data= {"FIELD1":"","nombre":name,"apellido":lastname,"usuario":user,"email":mail,"contraseña":password}
  datas = db.child("USUARIOS").child("2").set(data)
  return datas


#Retrieve data
def usuario_equal_usuario(var):
  db = firebase.database()
  usuarios = db.child("USUARIOS").order_by("usuario").equal_to('{}'.format(var)).get()
  filtro = usuarios.val()
  data = pd.DataFrame(filtro)
  change = data.transpose()
  usuario = change['usuario'].tolist()
  return usuario

def usuario_equal_contrasena(var):
  db = firebase.database()
  usuarios = db.child("USUARIOS").order_by("contraseña").equal_to('{}'.format(var)).get()
  filtro = usuarios.val()
  data = pd.DataFrame(filtro)
  change = data.transpose()
  contrasena = change['contraseña'].tolist()
  return contrasena


#ANALISIS Y LIMPIEZA DE DATOS

def df_filtered():
    db= database()
    date= db['fecha'].str.split('/',expand=True)
    date.columns = ['dia','mes','año']

    df = pd.concat([db,date],axis=1)
    return df

df =df_filtered()


#PÁGINA PRONOSTICOS
def funcion_1(estacion,mes,ano,df):
    #FILTRO
    filtro = df.query("año == @ano and idFinca == @estacion and mes == @mes")
    
    #DATA
    dia1= filtro['dia'].unique()
    precipitacion1 = pd.to_numeric(filtro['precipitacion'],errors='coerce')

    #LISTA DE DATOS A RETORNAR
    dias = dia1.tolist()
    preci_1= precipitacion1.tolist()

    return (dias,preci_1)

def funcion_2(estacion,mes,ano,df):
    #FILTRO
    filtro = df.query("año == @ano & mes == @mes and idFinca == @estacion")
    
    #DATA
    data =filtro['mes'].unique()
    data_1 = ''.join(data)
    
    data_2 = filtro['año'].unique()
    data_3 = ''.join(data_2)
    
    data_4 = filtro['idFinca'].unique()
    data_5 = ''.join(data_4)

    subset_df = filtro[filtro["precipitacion"]>'0']
    column_count = subset_df['precipitacion'].count()
    
    #LISTA DE DATOS A RETORNAR
    data1 = [data_5,data_1,data_3,column_count]
    label= ['estacion','mes','año','numero_de_días_con_lluvia']
    
    return (label,data1)

def funcion_3(estacion,ano,df):
    #FILTRO
    filtro = df.query("año == @ano and idFinca == @estacion")
    
    seleccion_columna_mes = filtro['mes']
    estacion = filtro['idFinca'].unique()
    
    #DATA
    columna_a_numeric = pd.to_numeric(filtro['precipitacion'],errors='coerce')
    concatenacion = pd.concat([seleccion_columna_mes,columna_a_numeric],axis=1)
    suma = concatenacion.groupby('mes').sum().precipitacion
    s_tota = [suma.sum()]
    total = ['TOTAL']
    concaten = total + s_tota
    
    #LISTA DE DATOS A RETORNAR
    data_2 = seleccion_columna_mes.unique()
    data_3 = data_2.tolist()
    val1 = suma.tolist()
    val2 = estacion.tolist()
    val3 = concaten

    return (data_3,val1, val2,val3)

#PÁGINA ESTACIONES
def funcion_4(estacion,mes,ano,df):
    #FILTRO
    filtro = df.query("año == @ano and idFinca == @estacion and mes == @mes ")
    
    #DATA
    dia0= filtro['dia']
    columna_a_numeric = pd.to_numeric(filtro['precipitacion'],errors='coerce')
    
    #LISTA DE DATOS A RETORNAR
    dia = dia0.tolist()
    precipitacion = columna_a_numeric.tolist()
    
    return (dia,precipitacion)

def funcion_5(estacion, mes,ano,df):
    #FILTRO
    filtro = df.query("año == @ano & mes == @mes & idFinca == @estacion")
    seleccion_columna_dia = filtro['dia']
    
    #DATA
    columna_a_numeric = pd.to_numeric(filtro['temperaturaMaxima'],errors='coerce')
    columna_a_numeric_1 = pd.to_numeric(filtro['temperaturaMinima'],errors='coerce')
    concatenacion = pd.concat([seleccion_columna_dia,columna_a_numeric,columna_a_numeric_1],axis=1)
    
    #LISTA DE DATOS A RETORNAR
    dia = concatenacion['dia'].tolist()
    tempmax = concatenacion['temperaturaMaxima'].tolist()
    tempmin = concatenacion['temperaturaMinima'].tolist()

    return (dia,tempmax,tempmin)

def funcion_6(estacion, mes,ano,df):
    #FILTRO
    filtro = df.query("año == @ano & mes == @mes & idFinca == @estacion")
    seleccion_columna_dia = filtro['dia']
    
    #DATA
    columna_a_numeric = pd.to_numeric(filtro['temperaturaMaxima'],errors='coerce')
    columna_a_numeric_1 = pd.to_numeric(filtro['temperaturaMinima'],errors='coerce')
    
    concatenacion = pd.concat([columna_a_numeric,columna_a_numeric_1],axis=1)
    
    variacion = concatenacion['temperaturaMaxima'] - concatenacion['temperaturaMinima']
    new_concat = pd.concat([seleccion_columna_dia,variacion],axis=1)
    new_concat.columns = ['dia','variacion']
    
    #LISTA DE DATOS A RETORNAR
    dia = new_concat['dia'].tolist()
    variacion = new_concat['variacion'].tolist()

    return (dia,variacion)

#GENERAL
def funcion_7(ano,df):
    #SUBCONJUNTO E1:
        #FILTRO
    filtro = df.query("año == @ano and idFinca == 'E1'") 
        #DATA
    seleccion_columna_mes = filtro[['mes','idFinca']]
    estacion0= filtro['idFinca'][:12]
    mes0= filtro['mes'].unique()
    columna_a_numeric = pd.to_numeric(filtro['precipitacion'],errors='coerce')
    concatenacion = pd.concat([seleccion_columna_mes,columna_a_numeric],axis=1)
    suma0 = concatenacion.groupby(['idFinca','mes']).sum().precipitacion
    
    #SUBCONJUNTO E2
        #FILTRO
    filtro = df.query("año == @ano and idFinca == 'E2'")    
        #DATA
    seleccion_columna_mes = filtro[['mes','idFinca']]
    estacion1= filtro['idFinca'][:12]
    mes1= filtro['mes'].unique()
    columna_a_numeric = pd.to_numeric(filtro['precipitacion'],errors='coerce')
    concatenacion = pd.concat([seleccion_columna_mes,columna_a_numeric],axis=1)
    suma1 = concatenacion.groupby(['idFinca','mes']).sum().precipitacion

    #SUBCONJUNTO E3
        #FILTRO
    filtro = df.query("año == @ano and idFinca == 'E3'")
        #DATA
    seleccion_columna_mes = filtro[['mes','idFinca']]
    estacion2= filtro['idFinca'][:12]
    mes2= filtro['mes'].unique()
    columna_a_numeric = pd.to_numeric(filtro['precipitacion'],errors='coerce')
    concatenacion = pd.concat([seleccion_columna_mes,columna_a_numeric],axis=1)
    suma2 = concatenacion.groupby(['idFinca','mes']).sum().precipitacion

    #SUBCONJUNTO E4
        #FILTRO
    filtro = df.query("año == @ano and idFinca == 'E4'")
        #DATA
    seleccion_columna_mes = filtro[['mes','idFinca']]
    estacion3= filtro['idFinca'][:12]
    mes3= filtro['mes'].unique()
    columna_a_numeric = pd.to_numeric(filtro['precipitacion'],errors='coerce')
    concatenacion = pd.concat([seleccion_columna_mes,columna_a_numeric],axis=1)
    suma3 = concatenacion.groupby(['idFinca','mes']).sum().precipitacion

    #SUBCONJUNTO E5
        #FILTRO
    filtro = df.query("año == @ano and idFinca == 'E5'")
        #DATA
    seleccion_columna_mes = filtro[['mes','idFinca']]
    estacion4= filtro['idFinca'][:12]
    mes4= filtro['mes'].unique()
    columna_a_numeric = pd.to_numeric(filtro['precipitacion'],errors='coerce')
    concatenacion = pd.concat([seleccion_columna_mes,columna_a_numeric],axis=1)
    suma4 = concatenacion.groupby(['idFinca','mes']).sum().precipitacion

    #SUBCONJUNTO E6
        #FILTRO
    filtro = df.query("año == @ano and idFinca == 'E6'")
        #DATA
    seleccion_columna_mes = filtro[['mes','idFinca']]
    estacion5= filtro['idFinca'][:12]
    mes5= filtro['mes'].unique()
    columna_a_numeric = pd.to_numeric(filtro['precipitacion'],errors='coerce')
    concatenacion = pd.concat([seleccion_columna_mes,columna_a_numeric],axis=1)
    suma5 = concatenacion.groupby(['idFinca','mes']).sum().precipitacion

    #SUBCONJUNTO E7
        #FILTRO
    filtro = df.query("año == @ano and idFinca == 'E7'")
        #DATA
    seleccion_columna_mes = filtro[['mes','idFinca']]
    estacion6= filtro['idFinca'][:12]
    mes6= filtro['mes'].unique()
    columna_a_numeric = pd.to_numeric(filtro['precipitacion'],errors='coerce')
    concatenacion = pd.concat([seleccion_columna_mes,columna_a_numeric],axis=1)
    suma6 = concatenacion.groupby(['idFinca','mes']).sum().precipitacion

    #LISTAS PARA RETORNAR
    labels = ['estaciones','mes','sumatoria precipitacion']
    estacion = estacion0.tolist() + estacion1.tolist() + estacion2.tolist() + estacion3.tolist() + estacion4.tolist() + estacion5.tolist() + estacion6.tolist()
    mes = mes0.tolist() + mes1.tolist() + mes2.tolist() + mes3.tolist() + mes4.tolist() + mes5.tolist() + mes6.tolist()
    suma = suma0.tolist() + suma1.tolist() + suma2.tolist() + suma3.tolist() + suma4.tolist() + suma5.tolist() + suma6.tolist()
    return (labels,estacion,mes,suma)

def funcion_8(ano,df):
    #SUBCONJUNTO E1:
        #FILTRO
    filtro = df.query("año == @ano and idFinca == 'E1'")
    seleccion_columna_mes = filtro[['mes','idFinca']]
    estacion1= filtro['idFinca'][:12]
    mes1= filtro['mes'].unique()
        #DATA
    columna_a_numeric = pd.to_numeric(filtro['temperaturaMaxima'],errors='coerce')
    columna_a_numeric1 = pd.to_numeric(filtro['temperaturaMinima'],errors='coerce')
    concatenacion = pd.concat([seleccion_columna_mes,columna_a_numeric],axis=1)
    concatenacion0 = pd.concat([seleccion_columna_mes,columna_a_numeric1],axis=1)
    suma1 = concatenacion.groupby(['idFinca','mes'])['temperaturaMaxima'].mean()
    suma0_1 = concatenacion0.groupby(['idFinca','mes'])['temperaturaMinima'].mean()
    
    #SUBCONJUNTO E2:
        #FILTRO
    filtro = df.query("año == @ano and idFinca == 'E2'")
    seleccion_columna_mes = filtro[['mes','idFinca']]
    estacion2= filtro['idFinca'][:12]
    mes2= filtro['mes'].unique()
        #DATA
    columna_a_numeric = pd.to_numeric(filtro['temperaturaMaxima'],errors='coerce')
    columna_a_numeric2 = pd.to_numeric(filtro['temperaturaMinima'],errors='coerce')
    concatenacion = pd.concat([seleccion_columna_mes,columna_a_numeric],axis=1)
    concatenacion2 = pd.concat([seleccion_columna_mes,columna_a_numeric2],axis=1)
    suma2 = concatenacion.groupby(['idFinca','mes'])['temperaturaMaxima'].mean()
    suma0_2 = concatenacion2.groupby(['idFinca','mes'])['temperaturaMinima'].mean()

    #SUBCONJUNTO E3:
        #FILTRO
    filtro = df.query("año == @ano and idFinca == 'E3'")
    seleccion_columna_mes = filtro[['mes','idFinca']]
    estacion3= filtro['idFinca'][:12]
    mes3= filtro['mes'].unique()
        #DATA    
    columna_a_numeric = pd.to_numeric(filtro['temperaturaMaxima'],errors='coerce')
    columna_a_numeric3 = pd.to_numeric(filtro['temperaturaMinima'],errors='coerce')
    concatenacion = pd.concat([seleccion_columna_mes,columna_a_numeric],axis=1)
    concatenacion3 = pd.concat([seleccion_columna_mes,columna_a_numeric3],axis=1)
    suma3 = concatenacion.groupby(['idFinca','mes'])['temperaturaMaxima'].mean()
    suma0_3 = concatenacion3.groupby(['idFinca','mes'])['temperaturaMinima'].mean()

    #SUBCONJUNTO E4:
        #FILTRO
    filtro = df.query("año == @ano and idFinca == 'E4'")
    seleccion_columna_mes = filtro[['mes','idFinca']]
    estacion4= filtro['idFinca'][:12]
    mes4= filtro['mes'].unique()
        #DATA    
    columna_a_numeric = pd.to_numeric(filtro['temperaturaMaxima'],errors='coerce')
    columna_a_numeric4 = pd.to_numeric(filtro['temperaturaMinima'],errors='coerce')
    concatenacion = pd.concat([seleccion_columna_mes,columna_a_numeric],axis=1)
    concatenacion4 = pd.concat([seleccion_columna_mes,columna_a_numeric4],axis=1)
    suma4 = concatenacion.groupby(['idFinca','mes'])['temperaturaMaxima'].mean()
    suma0_4 = concatenacion4.groupby(['idFinca','mes'])['temperaturaMinima'].mean()

    #SUBCONJUNTO E5:
        #FILTRO
    filtro = df.query("año == @ano and idFinca == 'E5'")
    seleccion_columna_mes = filtro[['mes','idFinca']]
    estacion5= filtro['idFinca'][:12]
    mes5= filtro['mes'].unique()
        #DATA    
    columna_a_numeric = pd.to_numeric(filtro['temperaturaMaxima'],errors='coerce')
    columna_a_numeric5 = pd.to_numeric(filtro['temperaturaMinima'],errors='coerce')
    concatenacion = pd.concat([seleccion_columna_mes,columna_a_numeric],axis=1)
    concatenacion5 = pd.concat([seleccion_columna_mes,columna_a_numeric5],axis=1)
    suma5 = concatenacion.groupby(['idFinca','mes'])['temperaturaMaxima'].mean()
    suma0_5 = concatenacion5.groupby(['idFinca','mes'])['temperaturaMinima'].mean()

    #SUBCONJUNTO E1:
        #FILTRO
    filtro = df.query("año == @ano and idFinca == 'E6'")
    seleccion_columna_mes = filtro[['mes','idFinca']]
    estacion6= filtro['idFinca'][:12]
    mes6= filtro['mes'].unique()
        #DATA    
    columna_a_numeric = pd.to_numeric(filtro['temperaturaMaxima'],errors='coerce')
    columna_a_numeric6 = pd.to_numeric(filtro['temperaturaMinima'],errors='coerce')
    concatenacion = pd.concat([seleccion_columna_mes,columna_a_numeric],axis=1)
    concatenacion6 = pd.concat([seleccion_columna_mes,columna_a_numeric6],axis=1)
    suma6 = concatenacion.groupby(['idFinca','mes'])['temperaturaMaxima'].mean()
    suma0_6 = concatenacion6.groupby(['idFinca','mes'])['temperaturaMinima'].mean()

    #SUBCONJUNTO E7:
        #FILTRO
    filtro = df.query("año == @ano and idFinca == 'E7'")
    seleccion_columna_mes = filtro[['mes','idFinca']]
    estacion7= filtro['idFinca'][:12]
    mes7= filtro['mes'].unique()
        #DATA
    columna_a_numeric = pd.to_numeric(filtro['temperaturaMaxima'],errors='coerce')
    columna_a_numeric7 = pd.to_numeric(filtro['temperaturaMinima'],errors='coerce')
    concatenacion = pd.concat([seleccion_columna_mes,columna_a_numeric],axis=1)
    concatenacion7 = pd.concat([seleccion_columna_mes,columna_a_numeric7],axis=1)
    suma7 = concatenacion.groupby(['idFinca','mes'])['temperaturaMaxima'].mean()
    suma0_7 = concatenacion7.groupby(['idFinca','mes'])['temperaturaMinima'].mean()

    #LISTAS PARA RETORNAR
    labels= ['estacion','mes','promedio temperatura máxima','promedio temperatura mínima']
    tempmax = suma1.tolist() + suma2.tolist() + suma3.tolist() + suma4.tolist() + suma5.tolist() + suma6.tolist() + suma7.tolist()
    tempmin = suma0_1.tolist() + suma0_2.tolist() + suma0_3.tolist() + suma0_4.tolist() + suma0_5.tolist() + suma0_6.tolist() + suma0_7.tolist()
    estaciones = estacion1.tolist() + estacion2.tolist() + estacion3.tolist() + estacion4.tolist() + estacion5.tolist() + estacion6.tolist() + estacion7.tolist()
    meses = mes1.tolist() + mes2.tolist() + mes3.tolist() + mes4.tolist() + mes5.tolist() + mes6.tolist() + mes7.tolist()

    return (labels,estaciones,meses,tempmax,tempmin)





def login_required(view):               #1 se define el decorador que coge el bloque de código de la función que querermos decorar
    @functools.wraps( view )            #2 utilizamos el módulo functools y la función .wrap para poder trabajar sobre otras funciones
    def wrapped_view(**kwargs):   #4 Revisamos si el usuario está o no en sesión, 
        if g.user is None:              
            flash('Primero necesitas iniciar sesión')     # 4.1 Si el usuario no está en sesión lo redireccionamos a la página de inicio de sesión
            return redirect( '/IniciarSesion/' )
        return view(**kwargs )                           #4.2 Si el usuario está en sesión, lo envía a la página (view) que solicitó
    return wrapped_view                 #3 retornamos /// llamamos a la funcion y retornamos su respuesta


#CONEXION BASE DATOS
def get_db():
    try:
        if "db" not in g:             #Se revisa si la variable "db" está dentro de las variables globales, si no lo está, se conecta a la base de datos
            g.db = firebase.database()
        return g.db
    except Exception as e:
        print(e)


def close_db():                 #En esta función se cierra la conexión a la base de datos
    db = g.pop( 'db', None )    

    if db is not None:
        db.close()

@app.before_request
def load_logged_in_user():
    user_id = session.get( "user_id" )

    if user_id is None:    
        g.user = None              
    else:
        g.user = usuario_equal_usuario(user_id)


@app.route('/')
def HOME():
  return render_template("HOME.html")

##Conexion a \templates\ventanaInicioSESION
@app.route('/IniciarSesion/', methods=('GET','POST'))
def iniciosesion():
  if g.user:
    return redirect( '/General/')
  if request.method == 'POST':
    usuario = request.form["usuario"]
    contrasena = request.form["contrasena"]
    user= usuario_equal_usuario(usuario)
    contraseña_bd = usuario_equal_contrasena(contrasena)
    if user is None or contraseña_bd is None:
      message = 'Usuario o contraseña Incorrectos'
      flash(message)
      return redirect('/IniciarSesion/')
    else:
      contraseña_b=contraseña_bd[0]
    if contrasena==contraseña_b :
      session.clear()
      session["user_id"] = user[0]
      flash('Ingresaste a la página')
      return  redirect('/General')
    else:
      flash('Contraseña incorrecta')
      return redirect('/IniciarSesion/')
  return render_template("ventanaInicioSESION.html")

##Conexion a \templates\ventanaRegistroUSUARIO
@app.route('/Registrarse/', methods=('GET','POST'))
def ventanaRegistroUSUARIO():
  if g.user:
    return redirect( '/' )
  try:
    if request.method == 'POST':
      nombre = request.form["nombre"]
      apellido = request.form["apellido"]
      usuario = request.form["usuario"]
      correo = request.form["email"]
      correo2 = request.form["email2"]
      contrasena = request.form["contrasena"]
      contrasena2 = request.form["contrasena2"]
      if correo == correo2 and contrasena == contrasena2:
        insert(nombre, apellido, usuario, correo, contrasena2)
        return redirect(url_for('iniciosesion'))
      else:
        flash('Correo o contraseñas no coinciden')
        return render_template("ventanaRegistroUSUARIO.html", nombre = nombre, Apellido = apellido, Usuario=usuario)
    return render_template("ventanaRegistroUSUARIO.html")
  except:
    flash('Este correo o usuario ya están registrados') 
    return render_template("ventanaRegistroUSUARIO.html")

##Conexion a \templates\PRONOSTICOS
@app.route('/Pronosticos/', methods=('GET','POST'))
def PRONOSTICOS():
    if request.method == 'POST':
        #GET DATA
        select_ano = request.form.get('ano')
        select_mes = request.form.get('mes')
        select_estacion = request.form.get('estacion')
        df= df_filtered()

        #FUNCION 1 DATA GRÁFICA
        fun_1 = funcion_1(select_estacion,select_mes, select_ano, df)
        labels1 = fun_1[0]
        preci1 = fun_1[1]

        #FUNCION 2 DATA TABLA 1
        fun_2 = funcion_2(select_estacion,select_mes, select_ano, df)
        labels_2 = fun_2[0] 
        year = fun_2[1] 
        
        #FUNCION 3 DATA TABLA 2
        fun_3 = funcion_3(select_estacion,select_ano, df)
        labels_3= ['mes','sumatoria precipitacion']
        month = fun_3[0]
        suma_precipitacion = fun_3[1]
        estacion = fun_3[2]
        total= fun_3[3][0]
        total1= fun_3[3][1]


        return render_template("PRONOSTICOS.html",labels1=labels1,labels2=labels_2,labels3=labels_3,values1=preci1,values2=year,values3=month,values4=suma_precipitacion,values5=estacion,values6=total,values7=total1)
    
    return render_template("PRONOSTICOS.html")

##Conexion a \templates\ESTACIONES
@app.route('/Estaciones/', methods=('GET', 'POST'))
def ESTACIONES():

    if request.method == 'POST':
        #GET DATA
        select_ano = request.form.get('ano')
        select_mes = request.form.get('mes')
        select_estacion = request.form.get('estacion')

        #FUNCIONES Y ASIGNACIÓN VARIABLES PARA RETORNO DE DATA
        df= df_filtered()
        
        #FUNCION 4 DATA GRÁFICA
        fun_4 = funcion_4(select_estacion,select_mes, select_ano, df)
        labels_6 = fun_4[0] 
        precipitacion = fun_4[1]

        #FUNCION 5 DATA GRÁFICA
        fun_5 = funcion_5(select_estacion, select_mes, select_ano, df)
        labels_7 = fun_5[0]
        tempmax = fun_5[1]
        tempmin = fun_5[2]

        #FUNCION 6 DATA GRÁFICA
        fun_6 = funcion_6(select_estacion, select_mes, select_ano, df)
        labels_8 = fun_6[0]
        variacion = fun_6[1]

        return render_template("ESTACIONES.html",labels6=labels_6,labels7=labels_7,labels8=labels_8,values14=precipitacion,values15=tempmax,values16=tempmin,values17=variacion)

    return render_template("ESTACIONES.html")

##Conexion a \templates\GENERAL
@app.route('/General/', methods=('GET','POST'))
@login_required
def GENERAL():

    if request.method == 'POST':
        #GET DATA
        select_ano = request.form.get('ano')
        
        #FUNCIONES Y ASIGNACIÓN VARIABLES PARA RETORNO DE DATA
        df= df_filtered()
        
        #FUNCION 7 DATA TABLA 1
        fun_7 = funcion_7(select_ano, df)
        labels_4 = fun_7[0]
        estaciones = fun_7[1]
        mes = fun_7[2]
        suma_precipitacion = fun_7[3]

        #FUNCION 8 DATA TABLA 2
        fun_8 = funcion_8(select_ano, df)
        labels_5 = fun_8[0]
        estacion = fun_8[1]
        month = fun_8[2]
        suma_tempmax = fun_8[3]
        suma_tempmin = fun_8[4]

        return render_template("GENERAL.html",labels4=labels_4,labels5=labels_5,values7=estaciones,values8=mes,values9=suma_precipitacion,values10=estacion,values11=month,values12=suma_tempmax,values13=suma_tempmin)

    return render_template("GENERAL.html")    

@app.route('/CerrarSesion/')
@login_required
def CerrarSesion():
  user_id = session.get( 'user_id' )
  session.clear()
  if user_id is not None:
      g.user = None
  if g.user is None:
    flash('Has cerrado sesión satisfactoriamente')
    return redirect('/')
  return redirect( '/IniciarSesion/' )

  
if __name__ == "__main__":
  app.run( host='0.0.0.0', debug=True, port=random.randint(2000, 9000) )
  