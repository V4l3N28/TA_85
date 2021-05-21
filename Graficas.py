import pandas as pd
import matplotlib.pyplot as plt

#Para importar un archivo de Excel a Python usaremos Pandas. Para lograr este objetivo, deberá utilizar read_excel.
#en la parte del camino hacia el archivo se tiene que cambiar segun el usuario.
registros = pd.read_excel(r"C:\Users\Isaac Mesa\OneDrive\Escritorio\UNIVERSIDAD\CURSANDO\FUNDAMETOS DE PROGRAMACIÓN\PROYECTO\virtualenvs\Python\TABLA REGISTROS.xlsx")
#Aca establecemos los nombres de las columnas de la tabla excel para python
dfr = pd.DataFrame(registros, columns=['idFinca','fecha','precipitacion','temperaturaMaxima','temperaturaMinima'])


#El método .loc con el que seleccionar filas o columnas en base a una etiqueta o seleccionar filas o columnas en base a una condición
# en los corchetes[:,] establecemos el numero de las filas y de cual columna queremos los datos especificos
# La función .sum() agrega los elementos de un iterable y devuelve la suma.
sum2011_idFinca1=dfr.loc[0:365, 'precipitacion'].sum()
print("la sumatoria total del ano 2011 de idFinca1 es: ",sum2011_idFinca1,"\n")

sum2012_idFinca1=dfr.loc[366:733, 'precipitacion'].sum()
print("la sumatoria total del ano 2012 de idFinca1 es: ",sum2012_idFinca1,"\n")

sum2013_idFinca1=dfr.loc[733:1098, 'precipitacion'].sum()
print("la sumatoria total del ano 2013 de idFinca1 es: ",sum2013_idFinca1,"\n")

sum2014_idFinca1=dfr.loc[1098:1462, 'precipitacion'].sum()
print("la sumatoria total del ano 2014 de idFinca1 es: ",sum2014_idFinca1,"\n")

sum2015_idFinca7=dfr.loc[6120:6150, 'precipitacion'].sum()
print("la sumatoria total del ano 2015 de idFinca1 es: ",sum2015_idFinca7,"\n")

#en la tabla se organiza la informacion dando prioridad al idFinca y no al año por lo tanto se hace necesario hager varias sum2016 ya que no se puede coger en un solo intervalo
# Esto tembien ayuda a organizar quien provee que informacion
sum2016_idFinca1=dfr.loc[1463:1829, 'precipitacion'].sum()
sum2016_idFinca4=dfr.loc[4167:4289, 'precipitacion'].sum()
sum2016_idFinca7=dfr.loc[6151:6516, 'precipitacion'].sum()

print("la sumatoria total del ano 2016 de idFinca1 es: ",sum2016_idFinca1)
print("la sumatoria total del ano 2016 de idFinca4 es: ",sum2016_idFinca4)
print("la sumatoria total del ano 2016 de idFinca7 es: ",sum2016_idFinca7,"\n")

sum2017_idFinca1=dfr.loc[1829:2194, 'precipitacion'].sum()
sum2017_idFinca3=dfr.loc[3164:3529, 'precipitacion'].sum()
sum2017_idFinca4=dfr.loc[4289:4654, 'precipitacion'].sum()
sum2017_idFinca7=dfr.loc[6517:6882, 'precipitacion'].sum()

print("la sumatoria total del ano 2017 de idFinca1 es: ",sum2017_idFinca1)
print("la sumatoria total del ano 2017 de idFinca3 es: ",sum2017_idFinca3)
print("la sumatoria total del ano 2017 de idFinca4 es: ",sum2017_idFinca4)
print("la sumatoria total del ano 2017 de idFinca7 es: ",sum2017_idFinca7,"\n")

sum2018_idFinca1=dfr.loc[2194:2559, 'precipitacion'].sum()
sum2018_idFinca2=dfr.loc[2830:2891, 'precipitacion'].sum()
sum2018_idFinca3=dfr.loc[3529:3894, 'precipitacion'].sum()
sum2018_idFinca4=dfr.loc[4654:5019, 'precipitacion'].sum()
sum2018_idFinca5=dfr.loc[5292:5448, 'precipitacion'].sum()
sum2018_idFinca6=dfr.loc[5725:5847, 'precipitacion'].sum()
sum2018_idFinca7=dfr.loc[6882:7248, 'precipitacion'].sum()

print("la sumatoria total del ano 2018 de idFinca1 es: ",sum2018_idFinca1)
print("la sumatoria total del ano 2018 de idFinca2 es: ",sum2018_idFinca2)
print("la sumatoria total del ano 2018 de idFinca3 es: ",sum2018_idFinca3)
print("la sumatoria total del ano 2018 de idFinca4 es: ",sum2018_idFinca4)
print("la sumatoria total del ano 2018 de idFinca5 es: ",sum2018_idFinca5)
print("la sumatoria total del ano 2018 de idFinca6 es: ",sum2018_idFinca6)
print("la sumatoria total del ano 2018 de idFinca7 es: ",sum2018_idFinca7,"\n")

sum2019_idFinca1=dfr.loc[2559:2830, 'precipitacion'].sum()
sum2019_idFinca2=dfr.loc[2891:3164, 'precipitacion'].sum()
sum2019_idFinca3=dfr.loc[3894:4167, 'precipitacion'].sum()
sum2019_idFinca4=dfr.loc[5019:5292, 'precipitacion'].sum()
sum2019_idFinca5=dfr.loc[5448:5725, 'precipitacion'].sum()
sum2019_idFinca6=dfr.loc[5847:6120, 'precipitacion'].sum()
sum2019_idFinca7=dfr.loc[7248:7521, 'precipitacion'].sum()

print("la sumatoria total del ano 2019 de idFinca1 es: ",sum2019_idFinca1)
print("la sumatoria total del ano 2019 de idFinca2 es: ",sum2019_idFinca2)
print("la sumatoria total del ano 2019 de idFinca3 es: ",sum2019_idFinca3)
print("la sumatoria total del ano 2019 de idFinca4 es: ",sum2019_idFinca4)
print("la sumatoria total del ano 2019 de idFinca5 es: ",sum2019_idFinca5)
print("la sumatoria total del ano 2019 de idFinca6 es: ",sum2019_idFinca6)
print("la sumatoria total del ano 2019 de idFinca7 es: ",sum2019_idFinca7,"\n")

"""promedio"""
"""por temas de exactitus se podria tratar estos promedios no solo por el año si no tambien por el idFinca
que entrego estos resultados, de esta manera tendiamos promedios anuales generales y promedios anuales especificos"""

#El método .loc con el que seleccionar filas o columnas en base a una etiqueta o seleccionar filas o columnas en base a una condición
# en los corchetes[:,] establecemos el numero de las filas y de cual columna queremos los datos especificos
#Con la funcion .mean() es posible calcular el promedio sobre una columna seleccionada
num2011_idFinca1=dfr.loc[0:365, 'precipitacion'].mean()
print("El promedio total del ano 2011 es: ",num2011_idFinca1,"\n")

num2012_idFinca1=dfr.loc[366:733, 'precipitacion'].mean()
print("El promedio total del ano 2012 es: ",num2012_idFinca1,"\n")

num2013_idFinca1=dfr.loc[733:1098, 'precipitacion'].mean()
print("El promedio total del ano 2013 es: ",num2013_idFinca1,"\n")

num2014_idFinca1=dfr.loc[1098:1462, 'precipitacion'].mean()
print("El promedio total del ano 2014 es: ",num2014_idFinca1,"\n")

num2015_idFinca7=dfr.loc[6120:6150, 'precipitacion'].mean()
print("El promedio total del ano 2015 es: ",num2015_idFinca7,"\n")

#en la tabla se organiza la informacion dando prioridad al idFinca y no al año por lo tanto se hace necesario hager varias sum2016 ya que no se puede coger en un solo intervalo
# Esto tembien ayuda a organizar quien provee que informacion

num2016_idFinca1=dfr.loc[1463:1829, 'precipitacion'].mean()
num2016_idFinca4=dfr.loc[4167:4289, 'precipitacion'].mean()
num2016_idFinca7=dfr.loc[6151:6516, 'precipitacion'].mean()

print("El promedio total del ano 2016 de idFinca1 es: ",num2016_idFinca1)
print("El promedio total del ano 2016 de idFinca4 es: ",num2016_idFinca4)
print("El promedio total del ano 2016 de idFinca7 es: ",num2016_idFinca7,"\n")

num2017_idFinca1=dfr.loc[1829:2194, 'precipitacion'].mean()
num2017_idFinca3=dfr.loc[3164:3529, 'precipitacion'].mean()
num2017_idFinca4=dfr.loc[4289:4654, 'precipitacion'].mean()
num2017_idFinca7=dfr.loc[6517:6882, 'precipitacion'].mean()

print("El promedio total del ano 2017 de idFinca1 es: ",num2017_idFinca1)
print("El promedio total del ano 2017 de idFinca3 es: ",num2017_idFinca3)
print("El promedio total del ano 2017 de idFinca4 es: ",num2017_idFinca4)
print("El promedio total del ano 2017 de idFinca7 es: ",num2017_idFinca7,"\n")

num2018_idFinca1=dfr.loc[2194:2559, 'precipitacion'].mean()
num2018_idFinca2=dfr.loc[2830:2891, 'precipitacion'].mean()
num2018_idFinca3=dfr.loc[3529:3894, 'precipitacion'].mean()
num2018_idFinca4=dfr.loc[4654:5019, 'precipitacion'].mean()
num2018_idFinca5=dfr.loc[5292:5448, 'precipitacion'].mean()
num2018_idFinca6=dfr.loc[5725:5847, 'precipitacion'].mean()
num2018_idFinca7=dfr.loc[6882:7248, 'precipitacion'].mean()

print("El promedio total del ano 2018 de idFinca1 es: ",num2018_idFinca1)
print("El promedio total del ano 2018 de idFinca2 es: ",num2018_idFinca2)
print("El promedio total del ano 2018 de idFinca3 es: ",num2018_idFinca3)
print("El promedio total del ano 2018 de idFinca4 es: ",num2018_idFinca4)
print("El promedio total del ano 2018 de idFinca5 es: ",num2018_idFinca5)
print("El promedio total del ano 2018 de idFinca6 es: ",num2018_idFinca6)
print("El promedio total del ano 2018 de idFinca7 es: ",num2018_idFinca7,"\n")

num2019_idFinca1=dfr.loc[2559:2830, 'precipitacion'].mean()
num2019_idFinca2=dfr.loc[2891:3164, 'precipitacion'].mean()
num2019_idFinca3=dfr.loc[3894:4167, 'precipitacion'].mean()
num2019_idFinca4=dfr.loc[5019:5292, 'precipitacion'].mean()
num2019_idFinca5=dfr.loc[5448:5725, 'precipitacion'].mean()
num2019_idFinca6=dfr.loc[5847:6120, 'precipitacion'].mean()
num2019_idFinca7=dfr.loc[7248:7521, 'precipitacion'].mean()

print("El promedio total del ano 2019 de idFinca1 es: ",num2019_idFinca1)
print("El promedio total del ano 2019 de idFinca2 es: ",num2019_idFinca2)
print("El promedio total del ano 2019 de idFinca3 es: ",num2019_idFinca3)
print("El promedio total del ano 2019 de idFinca4 es: ",num2019_idFinca4)
print("El promedio total del ano 2019 de idFinca5 es: ",num2019_idFinca5)
print("El promedio total del ano 2019 de idFinca6 es: ",num2019_idFinca6)
print("El promedio total del ano 2019 de idFinca7 es: ",num2019_idFinca7,"\n")


