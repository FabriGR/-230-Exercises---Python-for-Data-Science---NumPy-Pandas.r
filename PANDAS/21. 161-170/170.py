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

# Se agrupa el DataFrame por la columna 'year' y se cuenta el número de filas en cada grupo
# Esto se hace utilizando el método 'groupby()' seguido de 'size()'
# El resultado es una serie que muestra el tamaño de cada grupo de acuerdo al año
grouped_year_size = df.groupby('year').size()

# Se imprime el resultado, que muestra el tamaño de cada grupo de acuerdo al año
print(grouped_year_size)