"""
Exercise 149
The df DataFrame is given below. Extract first five rows of the df and convert into the dictionary as shown below.

In response, print this dictionary to the console.
"""

# 1 

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

# Imprimir un diccionario que contiene los primeros cinco elementos del DataFrame
print(df.head().to_dict())

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

# Imprimir un diccionario que contiene los primeros cinco elementos del DataFrame
print(df[:5].to_dict())
"""