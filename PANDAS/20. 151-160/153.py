"""
Exercise 153
The following DataFrame is given:

|   df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))

Iterate through the first five rows of this object and print each row to the console as shown below.

Tip: Use the pd.DataFrame.iterrows() function.
"""

# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd

# Establecer una semilla aleatoria para reproducibilidad
np.random.seed(42)

# Crear un DataFrame de 10 filas y 4 columnas con números aleatorios entre 0 y 1
# Las columnas se etiquetan como 'A', 'B', 'C', 'D'
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))

# Iterar sobre las primeras filas del DataFrame utilizando el método head() y el iterador iterrows()
# Imprimir cada fila
for index, row in df.head().iterrows():
    print(row)