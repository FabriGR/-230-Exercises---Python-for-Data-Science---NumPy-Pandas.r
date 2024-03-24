import numpy as np  # Se importa la biblioteca NumPy para operaciones numéricas
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
# Esto se hace utilizando una comprensión de lista y el método 'lower()' de las cadenas
df.columns = [col.lower() for col in df.columns]

# Se utiliza 'np.where()' para reemplazar los valores 'null bhp' en la columna 'power' con NaN (valores nulos)
# Esto se hace aplicando una condición a la columna 'power' y reemplazando los valores que cumplen la condición con NaN
df['power'] = np.where(df['power'] == 'null bhp', np.nan, df['power'])

# Se imprime el recuento de los 5 valores más comunes en la columna 'power' después de realizar las modificaciones
print(df['power'].value_counts()[:5])