import pandas as pd  # Se importa la biblioteca Pandas para manejo de datos tabulares

# Se define la URL del archivo CSV a cargar en el DataFrame
url = (
    'https://storage.googleapis.com/esmartdata-courses-files/'
    'dash-course/data.csv'
)

# Se carga el archivo CSV desde la URL en un DataFrame de Pandas llamado 'df'
# El parámetro 'index_col=0' se establece para utilizar la primera columna como índice del DataFrame
df = pd.read_csv(url, index_col=0)

# Se convierten los nombres de las columnas del DataFrame a minúsculas
# Esto se hace utilizando una comprensión de lista
df.columns = [col.lower() for col in df.columns]

# Se utiliza el método 'map()' para mapear los valores de la columna 'transmission'
# La cadena 'Manual' se mapea a 0 y 'Automatic' se mapea a 1
df['transmission'] = df['transmission'].map({'Manual': 0, 'Automatic': 1})

# Se imprime la serie que contiene los primeros valores de la columna 'transmission' después de la modificación
print(df['transmission'].head())