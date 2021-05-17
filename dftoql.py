#Se importan librerías de python como sqlite3, pandas y numpy. También se importan los DataFrame anteriormente creados en la hoja tablas.py
import sqlite3 
import pandas as pd
import numpy as np
import datetime
from tablas import veredas,registros,usuarios,fincas,observadores

#Se hace la conexión a la base de datos bases_07.db por medio de la asignación a una variable conn
conn=sqlite3.connect('bases_02.db')
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
df = pd.DataFrame(cursor, columns=['fecha','precipitacion'])

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

#Se imprimen las funciones para verificar su funcionamiento
print(sumatoria_prec(str(2011), df));print(promedio_prec(str(2011),df)); print(temp_max(str(2017), df)); print(temp_min(str(2017), df))


