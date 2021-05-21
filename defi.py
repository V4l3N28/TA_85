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

#Se define una funcion login_required() que va a ser usada para la gestion de las sesiones de usuario
#En caso de que no exita el usuario de la sesion, se le enviara al inicio de sesion
def login_required():
    if g.user is None:
        return redirect( url_for( 'ventanaInicioSESION' ) )
    return 