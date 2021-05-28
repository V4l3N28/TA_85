#Para crear una tabla a partir de un dataframe con matplotlib se utiliza una función
#.subplots la cual retorna una figura (fig) con un específico número de  ejes (ax =axes), los cuales definen la dimendión de la figura
# la función de la siguiente manera .subplots() define una dimensión de 1 ,1 (sería lo mismo si se escribe así .subplots(1,1))
fig, ax =plt.subplots()
#Se definen los nombres de las columnas con column_labels 
column_labels=["fecha", "precipitacion"]
#Se definen los datos creando una variable df y asignandole a esa variable el DataFrame que retorna la función sumatoria_prec en determinado año
df=sumatoria_prec(str(2011), df)
#ax.axis('tight') sirve para ajustar el espacio entre los datos del eje y el eje
ax.axis('tight')
#ax.axis('off') sirve para que en el gráfico no se muestren los ejes
ax.axis('off')
#ax.table() sirve para agregar una tabla en los ejes, dentro de los paréntesis se define
#el contenido de las celdas, el nombre de las columnas y la ubicación de aquella tabla dentro de la gráfica
ax.table(cellText=df.values,colLabels=df.columns,loc="center")
#Ahora definimos una variable a la cual de asignamos la función .show() que es la que muestra el gráfico
#sumatableshow = plt.show()

#En las siguientes líneas de código se hacen otras tablas de la misma manera que la anterior pero con diferentes funciones
fig, ax =plt.subplots(1,1)
column_labels=["fecha", "precipitacion"]
df=promedio_prec(str(2011), df)
ax.axis('tight')
ax.axis('off')
ax.table(cellText=df.values,colLabels=df.columns,loc="center")
#promtableshow = plt.show()

fig, ax =plt.subplots(1,1)
column_labels=["fecha", "temperaturaMaxima"]
df=temp_max(str(2017), df)
ax.axis('tight')
ax.axis('off')
ax.table(cellText=df.values,colLabels=df.columns,loc="center")
#maxtableshow = plt.show()

fig, ax =plt.subplots(1,1)
column_labels=["fecha", "temperaturaMinima"]
df=temp_min(str(2017), df)
ax.axis('tight')
ax.axis('off')
ax.table(cellText=df.values,colLabels=df.columns,loc="center")
#mintableshow = plt.show()
