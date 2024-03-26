'''Exercise 173
Using pandas load the london_bike.csv file into the DataFrame and assign to df variable:

https://storage.googleapis.com/esmartdata-courses-files/ds-bootcamp/london_bike.csv

In response print basic information about this DataFrame to the console. '''

import pandas as pd  # Se importa la biblioteca Pandas para manejo de datos tabulares

# Se define la URL del archivo CSV a cargar en el DataFrame
url = (
    'https://storage.googleapis.com/esmartdata-courses-files/'
    'ds-bootcamp/london_bike.csv'
)

# Se carga el archivo CSV desde la URL en un DataFrame de Pandas llamado 'df'
# El parámetro 'index_col=0' se establece para utilizar la primera columna como índice del DataFrame
df = pd.read_csv(url, index_col=0)

# Se utiliza el método 'info()' para imprimir información sobre el DataFrame
# Esto incluye nombres de columnas, tipos de datos de las columnas y recuento de valores no nulos en cada columna
df.info()