#EVIDENCIA INTENTOS DE FUNCIONALIDAD DE CÓDIGO:
En este código se intentó crear la definición de una función que debe hacer la sumatoria de los datos de una columna. 
Se hace la conexion a una base de datos, se crea un cursor y se le asigna a una variable pr
conn=sqlite3.connect('bases_02.db')
pr= conn.cursor()

Se crean tablas en sql con base en unos dataframe extraídos de otra hoja (tablas.py)
veredas.to_sql('veredas', conn)
observadores.to_sql('dfo', conn)
fincas.to_sql('fincas', conn)
registros.to_sql('registros', conn)
usuarios.to_sql('usuarios', conn)

Se crea un dataframe con respecto a una tabla de datos y se definieron sus columnas, también se cambia el formato de una de ellas a datatime
df = pd.DataFrame(pr, columns=['fecha','precipitacion'])
fechas = pd.to_datetime(df['fecha']) 

se crean dos variables rango_fecha_1 y rango_fecha_2 para almacenar datos de fecha en una posición indicada
#rango_fecha_1= str(fechas[1000])
#rango_fecha_2= str(fechas[2000])

se hace una impresion para verificar que los datos entén correctos
print(df)
print(fechas[2000])

Se agregan tres columnas a la tabla, ano, mes y dia, los cuales contienen los valores de una columna fecha por separado
df['ano'] = pd.DatetimeIndex(df['fecha']).year
df['ano'] +=1
df['mes'] = pd.DatetimeIndex(df['fecha']).month
df['dia'] = pd.DatetimeIndex(df['fecha']).day

Se le da formato a las dos variables anteriormente descritas para poder utilizarlas como variables en la definicion
rango_fecha_1= '{}-{}-{}'.format(df['ano'][1000], df['mes'][1000], df['dia'][1000])
rango_fecha_2= '{}-{}-{}'.format(df['ano'][2000], df['mes'][2000], df['dia'][2000])

Se define una funcion que debe obtener la sumatoria de los datos en una columna de un dataframe con base en dos datos pedidos 
def sum_prec(fecha1,fecha2,df):
    Se intentaron tres métodos de filtracion de datos
    En el primero se define una variable mark, la cual filtra los datos de una columna con respecto a dos condiciones, que los datos sean mayores o iguales que la variable1 y que además estos datos sean menor o iguales que la variable2, luego se localiza esta variable en el dataframe y se le asigna a una variable llamada fil.
    mark = (df['fecha'] >= fecha1) & (df['fecha'] <= fecha2)
    fil= df.loc[mask]

    En el segundo método, A la variable filtered_df se le asigna el filtro los datos de una columna que se encuentren dentro de un rango en un dataframe
    filtered_df =df.loc[df["fecha"].between(fecha1, fecha2)]

    En el tercer método, a la variable filtered se le asignan los valores localizados entre dos variables dentro del dataframe 
    #El método .loc con el que seleccionar filas o columnas en base a una etiqueta o seleccionar filas o columnas en base a una condición
    filtered=df.loc[fecha1:fecha2]

    Los siguientes métodos de sumatoria corresponden a los tres métodos de filtración anteriormente usados, en esta sumatoria se utiliza la función sum()
    s = filtered_df['precipitacion'].sum()
    s = filtered_df.loc[:, 'precipitacion'].sum()
    s = filtered_df['precipitacion'].sum()
    
    Se imprime la variable s para verificar la funcionalidad de la definicion
    print(s)

    Se retorna la base de datos filtrada
    return filtered_df

Este método no cumple con la definición deseada y por ello se decidió intentar otro método el cual tuvo mejores resultados.