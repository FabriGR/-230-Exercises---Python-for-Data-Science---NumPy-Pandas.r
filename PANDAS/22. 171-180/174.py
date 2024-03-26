'''Exercise 174
The df DataFrame is given below. Print the first and last five rows of this object and look at the data. '''

import pandas as pd  # Se importa la biblioteca Pandas para manejo de datos tabulares

# Se configuran las opciones de visualización de Pandas
pd.set_option('max_columns', 9)  # Se establece el número máximo de columnas que se mostrarán en la salida
pd.set_option('display.width', 150)  # Se establece el ancho máximo de la salida

# Se define la URL del archivo CSV a cargar en el DataFrame
url = (
    'https://storage.googleapis.com/esmartdata-courses-files/'
    'ds-bootcamp/london_bike.csv'
)

# Se carga el archivo CSV desde la URL en un DataFrame de Pandas llamado 'df'
# El parámetro 'index_col=0' se establece para utilizar la primera columna como índice del DataFrame
df = pd.read_csv(url, index_col=0)

# Se imprime las primeras 5 filas del DataFrame
print(df.head())

# Se imprime las últimas 5 filas del DataFrame
print(df.tail())