""""
Exercise 148
The df DataFrame is given below. Extract rows for which the col2 takes values greater than 0.0 and print result to the console.
"""

# Importar las librerías necesarias
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

# Imprimir las filas del DataFrame donde los valores en 'col2' son mayores que 0
print(df.query("col2 > 0"))
