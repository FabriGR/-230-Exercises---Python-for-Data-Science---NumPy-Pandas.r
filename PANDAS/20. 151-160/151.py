"""
Exercise 151
The following DataFrame is given:

|   df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))

Extract rows of this DataFrame for which the C column is greater than 0.8 and print result to the console.
"""

# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd

# Establecer una semilla aleatoria para reproducibilidad
np.random.seed(42)

# Crear un DataFrame de 10 filas y 4 columnas con números aleatorios entre 0 y 1
# Las columnas se etiquetan como 'A', 'B', 'C', 'D'
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))

# Imprimir las filas del DataFrame donde los valores en la columna 'C' son mayores que 0.8
print(df.loc[df['C'] > 0.8])