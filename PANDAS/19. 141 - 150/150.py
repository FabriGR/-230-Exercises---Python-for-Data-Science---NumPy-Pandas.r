"""
Exercise 150
The df DataFrame is given below. Extract the first five rows of this object, convert to HTML and assign it to the df_html variable.

Print the contents of the df_html variable to the console
"""
#1

# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd

# Establecer una semilla aleatoria para reproducibilidad
np.random.seed(42)

# Crear una serie de Pandas con 20 números aleatorios entre 0 y 1
s1 = pd.Series(np.random.rand(20))

# Crear otra serie de Pandas con 20 números aleatorios distribuidos normalmente
s2 = pd.Series(np.random.randn(20))

# Concatenar las dos series en un DataFrame a lo largo del eje 1 (columnas)
df = pd.concat([s1, s2], axis=1)

# Renombrar las columnas del DataFrame como 'col1' y 'col2'
df.columns = ['col1', 'col2']

# Imprimir una representación HTML de las primeras cinco filas del DataFrame
print(df.head().to_html())

# 2

"""
# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd

# Establecer una semilla aleatoria para reproducibilidad
np.random.seed(42)

# Crear una serie de Pandas con 20 números aleatorios entre 0 y 1
s1 = pd.Series(np.random.rand(20))

# Crear otra serie de Pandas con 20 números aleatorios distribuidos normalmente
s2 = pd.Series(np.random.randn(20))

# Concatenar las dos series en un DataFrame a lo largo del eje 1 (columnas)
df = pd.concat([s1, s2], axis=1)

# Renombrar las columnas del DataFrame como 'col1' y 'col2'
df.columns = ['col1', 'col2']

# Imprimir una representación HTML de las primeras cinco filas del DataFrame
print(df[:5].to_html())
"""