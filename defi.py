import sqlite3
from sqlite3 import Error
from flask import current_app, g, url_for, redirect
import functools
import pandas as pd


#Se define una funcion get_db() en donde se utiliza un bloque try except el cual captura un error en el caso de que suceda
#Dentro de try abrimos un condicional if en donde verificamos si una variable 'db' no está en g (variables globales)
# si 'db' no está en g, entonces nos conectamos a la base de datos y le asignamos db a las variables globales
def get_db():
    try:
        if 'db' not in g:
            g.db = sqlite3.connect('bases_0704.db')
        return g.db
    except Error:
        print(Error)

#Se define una funcion close_db() en donde borramos db de las variables globales y verificamos si esa variable fue borrada
#Luego cerramos la base de datos
def close_db():
    db = g.pop( 'db', None )

    if db is not None:
        db.close()

#Se define una funcion login_required() que va a ser usada para la gestion de las sesiones de usuario
#En caso de que no exita el usuario de la sesion, se le enviara al inicio de sesion
def login_required():
    if g.user is None:
        return redirect( url_for( 'ventanaInicioSESION' ) )
    return 




"""en este espacio se subira lo que vendria a ser las formulas con las que trataremos las tablas de excel"""

"""en este espacio se hace las sumatoria anual de precipitaciones"""
#Para importar un archivo de Excel a Python usaremos Pandas. Para lograr este objetivo, deberá utilizar read_excel.
registros = pd.read_excel(
    r"C:\Users\valen\OneDrive\Escritorio\TABLA REGISTROS.xlsx")
#Aca establecemos los nombres de las columnas de la tabla excel para python
dfr = pd.DataFrame(registros, columns=[
                   'idFinca', 'fecha', 'precipitacion', 'temperaturaMaxima', 'temperaturaMinima'])
dfr = dfr.fillna('null')

#El método .loc con el que seleccionar filas o columnas en base a una etiqueta o seleccionar filas o columnas en base a una condición
# en los corchetes[:,] establecemos el numero de las filas y de cual columna queremos los datos especificos
# La función .sum() agrega los elementos de un iterable y devuelve la suma.
sum2011 = dfr.loc[0:365, 'precipitacion'].sum()
print("la sumatoria total del año 2011 es: ", sum2011)

sum2012 = dfr.loc[366:733, 'precipitacion'].sum()
print("la sumatoria total del año 2012 es: ", sum2012)

sum2013 = dfr.loc[733:1098, 'precipitacion'].sum()
print("la sumatoria total del año 2013 es: ", sum2013)

sum2014 = dfr.loc[1098:1462, 'precipitacion'].sum()
print("la sumatoria total del año 2014 es: ", sum2014)

sum2015 = dfr.loc[6120:6150, 'precipitacion'].sum()
print("la sumatoria total del año 2015 es: ", sum2015)

#en la tabla se organiza la informacion dando prioridad al idFinca y no al año por lo tanto se hace necesario hager varias sum2016 ya que no se puede coger en un solo intervalo
# Esto tembien ayuda a organizar quien provee que informacion
sum2016_idFinca1 = dfr.loc[1463:1829, 'precipitacion'].sum()
sum2016_idFinca4 = dfr.loc[4167:4289, 'precipitacion'].sum()
sum2016_idFinca7 = dfr.loc[6151:6516, 'precipitacion'].sum()

print("la sumatoria total del año 2016 es: ",
      sum2016_idFinca1+sum2016_idFinca4+sum2016_idFinca7)

sum2017_idFinca1 = dfr.loc[1829:2194, 'precipitacion'].sum()
sum2017_idFinca3 = dfr.loc[3164:3529, 'precipitacion'].sum()
sum2017_idFinca4 = dfr.loc[4289:4654, 'precipitacion'].sum()
sum2017_idFinca7 = dfr.loc[6517:6882, 'precipitacion'].sum()

print("la sumatoria total del año 2017 es: ", sum2017_idFinca1 +
      sum2017_idFinca3+sum2017_idFinca4+sum2017_idFinca7)

sum2018_idFinca1 = dfr.loc[2194:2559, 'precipitacion'].sum()
sum2018_idFinca2 = dfr.loc[2830:2891, 'precipitacion'].sum()
sum2018_idFinca3 = dfr.loc[3529:3894, 'precipitacion'].sum()
sum2018_idFinca4 = dfr.loc[4654:5019, 'precipitacion'].sum()
sum2018_idFinca5 = dfr.loc[5292:5448, 'precipitacion'].sum()
sum2018_idFinca6 = dfr.loc[5725:5847, 'precipitacion'].sum()
sum2018_idFinca7 = dfr.loc[6882:7248, 'precipitacion'].sum()

print("la sumatoria total del año 2018 es: ", sum2018_idFinca1+sum2018_idFinca2 +
      sum2018_idFinca3+sum2018_idFinca4+sum2018_idFinca5+sum2018_idFinca6+sum2018_idFinca7)

sum2019_idFinca1 = dfr.loc[2559:2830, 'precipitacion'].sum()
sum2019_idFinca2 = dfr.loc[2891:3164, 'precipitacion'].sum()
sum2019_idFinca3 = dfr.loc[3894:4167, 'precipitacion'].sum()
sum2019_idFinca4 = dfr.loc[5019:5292, 'precipitacion'].sum()
sum2019_idFinca5 = dfr.loc[5448:5725, 'precipitacion'].sum()
sum2019_idFinca6 = dfr.loc[5847:6120, 'precipitacion'].sum()
sum2019_idFinca7 = dfr.loc[7248:7521, 'precipitacion'].sum()

print("la sumatoria total del año 2019 es: ", sum2019_idFinca1+sum2019_idFinca2 +
      sum2019_idFinca3+sum2019_idFinca4+sum2019_idFinca5+sum2019_idFinca6+sum2019_idFinca7)
