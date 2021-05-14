import pandas as pd 
import numpy as np
#Importamos valores de un archivo de excel para para crear pandas de DataFrame, y utilizamos lo siguiente...

#data = pd.read_excel(path)
#df= pd.DataFrame(data, columns=[])

#Utilizamos lo anterior para crear nuestros DataFrame de usuarios, fincas, observadores, veredas y registros registros.
#En data llamamos a la carpeta de excel y le ponemos esa r al inicio para que lea bien, y en df agregamos sus columnas.


#DATAFRAME USUARIOS
dfu = pd.read_excel(r"C:\Users\valen\OneDrive\Escritorio\TABLA USUARIOS.xlsx")
usuarios = pd.DataFrame(dfu, columns=['nombre','apellido','usuario','email','contrasena'])
usuarios= usuarios.fillna('null')
usuarios.set_index('nombre',inplace = True)

#DATAFRAME FINCAS
dff = pd.read_excel(r"C:\Users\valen\OneDrive\Escritorio\TABLA FINCAS.xlsx")
fincas = pd.DataFrame(dff,columns=['idArea','finca'])
fincas= fincas.fillna('null')
fincas.set_index('idArea',inplace = True)

#DATAFRAME OBSERVADORES
dfo = pd.read_excel(r"C:\Users\valen\OneDrive\Escritorio\TABLA OBSERVADORES.xlsx")
observadores = pd.DataFrame(dfo, columns=['primerNombre','segundoNombre','apellidos','celular','latitud','longitud'])
observadores= observadores.fillna('null')
observadores.set_index('primerNombre',inplace = True)

#DATAFRAME VEREDAS
dfv = pd.read_excel(r"C:\Users\valen\OneDrive\Escritorio\TABLA VEREDAS.xlsx")
veredas = pd.DataFrame(dfv, columns=['departamento','ciudad','vereda'])
veredas= veredas.fillna('null')
veredas.set_index('departamento',inplace = True)

#DATAFRAME REGISTROS
dfr = pd.read_excel(r"C:\Users\valen\OneDrive\Escritorio\TABLA REGISTROS.xlsx")
registros = pd.DataFrame(dfr, columns=['idFinca','fecha','precipitacion','temperaturaMaxima','temperaturaMinima'])
#hacer que una columna sea el índice 
# dataframe.set_index(Column_name,inplace = True)
registros.set_index('idFinca',inplace = True)
registros= registros.fillna('null')
