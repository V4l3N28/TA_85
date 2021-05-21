import pandas as pd
import matplotlib.pyplot as plt
from dftoql import sumatoria_prec,promedio_prec,temp_max,temp_min,df

#Se le asigna a una variable llamada suma, una función
suma= sumatoria_prec(str(2011), df)
#Se le asigna a una variable llamada grafica el gráfico de la anterior variable por medio de una función plot, la cual define los valores de la columna fecha en el eje x
#y también define los valores de la columna precipitacion en el eje y. Se define el tipo de gráfico por medio de kind= y se pide que el tipo de gráfico sea en líneas
grafica = suma.plot(x='fecha', y='precipitacion', kind = 'line')
#Se le asigna a una variable llamada sumshow la funcion .show() que se encarga de mostrar el gráfico
sumshow = plt.show()

#Se hace el mismo método anterior para las funciones contenidas en prom,maxi y mini
prom= promedio_prec(str(2011), df)
grafica = prom.plot(x='fecha', y='precipitacion', kind = 'line')
promshow = plt.show()

maxi = temp_max(str(2017), df)
grafica = maxi.plot(x='fecha', y='temperaturaMaxima', kind = 'bar')
maxishow = plt.show()

mini = temp_min(str(2017), df)
grafica = mini.plot(x='fecha', y='temperaturaMinima', kind = 'bar')
minishow = plt.show()

#Para importar un archivo de Excel a Python usaremos Pandas. Para lograr este objetivo, deberá utilizar read_excel.
#en la parte del camino hacia el archivo se tiene que cambiar segun el usuario.
registros = pd.read_excel(r"TABLA REGISTROS.xlsx")
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


''' En esta parte se trabajaran las futuras graficas con las cuales se analizara los datos con una comparacion mucho mas facil''' 
#esta parte se uso para verificar el typo de respuesta con el que estamos trabajando ya que no estaba mostrando errores
# esta es la funcion de type() la cual se usa para revelar como se esta tratando una variable en el codigo 
# en este caso vimos que estabamos trabajando con valores numpy.float64 los cuales no eran aceptados por la tabla
# Use .item () para convertir la mayoría de los valores de NumPy a un tipo nativo de Python 
print(type(sum2011_idFinca1),"\n")
print(type(sum2011_idFinca1.item()),"\n")

''' graficas idFinca1'''

#en este apartado renombramos las variables segun su año y el usuario que lo proporciono con la finalidad de cambiar de numpy.float64 a float
#las variables de cada grafica se iran cambiando segun la cantidad de informacion que provea el usuario en cuanto a la recoleccion de los años
graf_sum2011_idFinca1=sum2011_idFinca1.item()
graf_sum2012_idFinca1=sum2012_idFinca1.item()
graf_sum2013_idFinca1=sum2013_idFinca1.item()
graf_sum2014_idFinca1=sum2014_idFinca1.item()
''' como el 2015 solo tiene un mes de informacion y fue ingresado por idFinca7 se pondra en su respectiva grafica a pesar de la falta de informacion'''
graf_sum2016_idFinca1=sum2016_idFinca1.item()
graf_sum2017_idFinca1=sum2017_idFinca1.item()
graf_sum2018_idFinca1=sum2018_idFinca1.item()
graf_sum2019_idFinca1=sum2019_idFinca1.item()

#verificamos que si cambio correctamente
print(type(graf_sum2011_idFinca1),"\n")

ano = ['A.2011','A.2012','2013','A.2014','A.2016','A.2017','A.2018','A.2019']
Sum_Anual = [graf_sum2011_idFinca1,
            graf_sum2012_idFinca1,
            graf_sum2013_idFinca1,
            graf_sum2014_idFinca1,
            graf_sum2016_idFinca1,
            graf_sum2017_idFinca1,
            graf_sum2018_idFinca1,
            graf_sum2019_idFinca1]

#en esta linea declaramos el nombre de las barras que vamos a usar
plt.bar(ano, Sum_Anual)
#definimos el titulo de la grafica
plt.title('Sumatoria de precipitaciones anuales de idFinca1')
#definimos el nombre del eje x
plt.xlabel('ano')
#definimos el nombre del eje y
plt.ylabel('total precipitaciones idFinca1')
#normalmente con solo poner plt.show() declaramos que nos muestre el final de la grafica
#decidimos en vez de mostrar el final de la grafica darle un codigo con el cual lo mostraremos segun nuestra necesidad mediante el print
graf_sum_idFinca1=plt.show()





''' graficas idFinca2'''

graf_sum2018_idFinca2=sum2018_idFinca2.item()
graf_sum2019_idFinca2=sum2019_idFinca2.item()

ano = ['A.2018','A.2019']
Sum_Anual = [graf_sum2018_idFinca2,
            graf_sum2019_idFinca2]

plt.bar(ano, Sum_Anual)
plt.title('Sumatoria de precipitaciones anuales de idFinca2')
plt.xlabel('ano')
plt.ylabel('total precipitaciones idFinca2')
graf_sum_idFinca2=plt.show()




''' graficas idFinca3'''

graf_sum2017_idFinca3=sum2017_idFinca3.item()
graf_sum2018_idFinca3=sum2018_idFinca3.item()
graf_sum2019_idFinca3=sum2019_idFinca3.item()

ano = ['A.2017','A.2018','A.2019']
Sum_Anual = [graf_sum2017_idFinca3,
            graf_sum2018_idFinca3,
            graf_sum2019_idFinca3]

plt.bar(ano, Sum_Anual)
plt.title('Sumatoria de precipitaciones anuales de idFinca3')
plt.xlabel('ano')
plt.ylabel('total precipitaciones idFinca3')
graf_sum_idFinca3=plt.show()




''' graficas idFinca4'''

graf_sum2016_idFinca4=sum2016_idFinca4.item()
graf_sum2017_idFinca4=sum2017_idFinca4.item()
graf_sum2018_idFinca4=sum2018_idFinca4.item()
graf_sum2019_idFinca4=sum2019_idFinca4.item()

ano = ['A.2016','A.2017','A.2018','A.2019']
Sum_Anual = [graf_sum2016_idFinca4,
            graf_sum2017_idFinca4,
            graf_sum2018_idFinca4,
            graf_sum2019_idFinca4]

plt.bar(ano, Sum_Anual)
plt.title('Sumatoria de precipitaciones anuales de idFinca4')
plt.xlabel('ano')
plt.ylabel('total precipitaciones idFinca4')
graf_sum_idFinca4=plt.show()




''' graficas idFinca5'''

graf_sum2018_idFinca5=sum2018_idFinca5.item()
graf_sum2019_idFinca5=sum2019_idFinca5.item()

ano = ['A.2018','A.2019']
Sum_Anual = [graf_sum2018_idFinca5,
            graf_sum2019_idFinca5]

plt.bar(ano, Sum_Anual)
plt.title('Sumatoria de precipitaciones anuales de idFinca5')
plt.xlabel('ano')
plt.ylabel('total precipitaciones idFinca5')
graf_sum_idFinca5=plt.show()




''' graficas idFinca6'''

graf_sum2018_idFinca6=sum2018_idFinca6.item()
graf_sum2019_idFinca6=sum2019_idFinca6.item()

ano = ['A.2018','A.2019']
Sum_Anual = [graf_sum2018_idFinca6,
            graf_sum2019_idFinca6]

plt.bar(ano, Sum_Anual)
plt.title('Sumatoria de precipitaciones anuales de idFinca6')
plt.xlabel('ano')
plt.ylabel('total precipitaciones idFinca6')
graf_sum_idFinca6=plt.show()




''' graficas idFinca7'''

graf_sum2015_idFinca7=sum2015_idFinca7.item()
graf_sum2016_idFinca7=sum2016_idFinca7.item()
graf_sum2017_idFinca7=sum2017_idFinca7.item()
graf_sum2018_idFinca7=sum2018_idFinca7.item()
graf_sum2019_idFinca7=sum2019_idFinca7.item()


ano = ['M.2015','A.2016','A.2017','A.2018','A.2019']
Sum_Anual = [graf_sum2015_idFinca7,
            graf_sum2016_idFinca7,
            graf_sum2017_idFinca7,
            graf_sum2018_idFinca7,
            graf_sum2019_idFinca7]

plt.bar(ano, Sum_Anual)
plt.title('Sumatoria de precipitaciones anuales de idFinca7')
plt.xlabel('ano')
plt.ylabel('total precipitaciones idFinca7')
graf_sum_idFinca7=plt.show()

#en este apartado mostraremos todas las tablas mediante su propio codigo y el uso de print()
print(graf_sum_idFinca1)
print(graf_sum_idFinca2)
print(graf_sum_idFinca3)
print(graf_sum_idFinca4)
print(graf_sum_idFinca5)
print(graf_sum_idFinca6)
print(graf_sum_idFinca7)

'''Graficas del promedio anual de precipitaciones'''
''' graficas idFinca1'''

#en este apartado renombramos las variables segun su año y el usuario que lo proporciono con la finalidad de cambiar de numpy.float64 a float
#las variables de cada grafica se iran cambiando segun la cantidad de informacion que provea el usuario en cuanto a la recoleccion de los años
graf_num2011_idFinca1=num2011_idFinca1.item()
graf_num2012_idFinca1=num2012_idFinca1.item()
graf_num2013_idFinca1=num2013_idFinca1.item()
graf_num2014_idFinca1=num2014_idFinca1.item()
graf_num2016_idFinca1=num2016_idFinca1.item()
graf_num2017_idFinca1=num2017_idFinca1.item()
graf_num2018_idFinca1=num2018_idFinca1.item()
graf_num2019_idFinca1=num2019_idFinca1.item()

#verificamos que si cambio correctamente
print(type(graf_sum2011_idFinca1),"\n")

ano = ['A.2011','A.2012','2013','A.2014','A.2016','A.2017','A.2018','A.2019']
Prom_Anual = [graf_num2011_idFinca1,
            graf_num2012_idFinca1,
            graf_num2013_idFinca1,
            graf_num2014_idFinca1,
            graf_num2016_idFinca1,
            graf_num2017_idFinca1,
            graf_num2018_idFinca1,
            graf_num2019_idFinca1]

plt.bar(ano, Prom_Anual)
plt.title('Promedio de precipitaciones anuales de idFinca1')
plt.xlabel('ano')
plt.ylabel('Promedio de precipitaciones idFinca1')
graf_num_idFinca1=plt.show()


''' graficas idFinca2'''

graf_num2018_idFinca2=num2018_idFinca2.item()
graf_num2019_idFinca2=num2019_idFinca2.item()

ano = ['A.2018','A.2019']
Prom_Anual = [graf_num2018_idFinca2,
            graf_num2019_idFinca2]

plt.bar(ano, Prom_Anual)
plt.title('Promedio de precipitaciones anuales de idFinca2')
plt.xlabel('ano')
plt.ylabel('Promedio de precipitaciones idFinca2')
graf_num_idFinca2=plt.show()


''' graficas idFinca3'''

graf_num2017_idFinca3=num2017_idFinca3.item()
graf_num2018_idFinca3=num2018_idFinca3.item()
graf_num2019_idFinca3=num2019_idFinca3.item()

ano = ['A.2017','A.2018','A.2019']
Prom_Anual = [graf_num2017_idFinca3,
            graf_num2018_idFinca3,
            graf_num2019_idFinca3]

plt.bar(ano, Prom_Anual)
plt.title('Promedio de precipitaciones anuales de idFinca3')
plt.xlabel('ano')
plt.ylabel('Promedio de precipitaciones idFinca3')
graf_num_idFinca3=plt.show()


''' graficas idFinca4'''

graf_num2016_idFinca4=num2016_idFinca4.item()
graf_num2017_idFinca4=num2017_idFinca4.item()
graf_num2018_idFinca4=num2018_idFinca4.item()
graf_num2019_idFinca4=num2019_idFinca4.item()

ano = ['A.2016','A.2017','A.2018','A.2019']
Prom_Anual = [graf_num2016_idFinca4,
            graf_num2017_idFinca4,
            graf_num2018_idFinca4,
            graf_num2019_idFinca4]

plt.bar(ano, Prom_Anual)
plt.title('Promedio de precipitaciones anuales de idFinca4')
plt.xlabel('ano')
plt.ylabel('Promedio de precipitaciones idFinca4')
graf_num_idFinca4=plt.show()


''' graficas idFinca5'''

graf_num2018_idFinca5=num2018_idFinca5.item()
graf_num2019_idFinca5=num2019_idFinca5.item()

ano = ['A.2018','A.2019']
Prom_Anual = [graf_num2018_idFinca5,
            graf_num2019_idFinca5]

plt.bar(ano, Prom_Anual)
plt.title('Promedio de precipitaciones anuales de idFinca5')
plt.xlabel('ano')
plt.ylabel('Promedio de precipitaciones idFinca5')
graf_num_idFinca5=plt.show()


''' graficas idFinca6'''

graf_num2018_idFinca6=num2018_idFinca6.item()
graf_num2019_idFinca6=num2019_idFinca6.item()

ano = ['A.2018','A.2019']
Prom_Anual = [graf_num2018_idFinca6,
            graf_num2019_idFinca6]

plt.bar(ano, Prom_Anual)
plt.title('Promedio de precipitaciones anuales de idFinca6')
plt.xlabel('ano')
plt.ylabel('Promedio de precipitaciones idFinca6')
graf_num_idFinca6=plt.show()


''' graficas idFinca7'''

graf_num2015_idFinca7=num2015_idFinca7.item()
graf_num2016_idFinca7=num2016_idFinca7.item()
graf_num2017_idFinca7=num2017_idFinca7.item()
graf_num2018_idFinca7=num2018_idFinca7.item()
graf_num2019_idFinca7=num2019_idFinca7.item()


ano = ['M.2015','A.2016','A.2017','A.2018','A.2019']
Prom_Anual = [graf_num2015_idFinca7,
            graf_num2016_idFinca7,
            graf_num2017_idFinca7,
            graf_num2018_idFinca7,
            graf_num2019_idFinca7]

plt.bar(ano, Prom_Anual)
plt.title('Promedio de precipitaciones anuales de idFinca7')
plt.xlabel('ano')
plt.ylabel('Promedio de precipitaciones idFinca7')
graf_num_idFinca7=plt.show()
