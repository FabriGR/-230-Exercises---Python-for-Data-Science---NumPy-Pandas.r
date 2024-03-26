'''Exercise 175
The df DataFrame is given below. Note that the timestamp column is of object type. Change it to datetime type.

Using the pd.DataFrame.info() print some information about this DataFrame to the console.

Tip: Use the pd.to_datetime() function. '''

import pandas as pd

# Enhanced readability and error handling
try:
  pd.set_option('display.max_columns', 9)  # Clear column display limit
  pd.set_option('display.width', 150)      # Wider output for better readability

  url = 'https://storage.googleapis.com/esmartdata-courses-files/ds-bootcamp/london_bike.csv'
  df = pd.read_csv(url)

  # Improved data type inference and potential missing value handling
  df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')  # Attempt conversion even for invalid types

  # Informative data exploration and insights
  print(df.info())  # Essential data type and memory usage overview

  # Optional: Descriptive statistics or visualizations for deeper understanding
  print(df.describe(include='all'))  # Summary statistics for various data types
  # Consider creating visualizations (histograms, boxplots, etc.) to explore data distribution

except Exception as e:
  print(f"An error occurred while processing the data: {e}")  # Informative error message

# Additional considerations (tailored to user's needs)
# - Data cleaning (handling outliers, inconsistencies)
# - Feature engineering (creating new features)
# - Exploratory data analysis (relationships between variables)