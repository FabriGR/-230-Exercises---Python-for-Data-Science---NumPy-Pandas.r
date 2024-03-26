'''Exercise 177
The df DataFrame is given below. Extract month from the timestamp column and assign to the new column 'month'. Print the first five rows of this DataFrame to the console. '''

# Import the pandas library for data analysis
import pandas as pd

# Set pandas display options for better readability
#  - max_columns limits the number of columns displayed at once
#  - display.width controls the overall width of the output
pd.set_option('max_columns', 15)
pd.set_option('display.width', 150)

# Define the URL where the London bike data is stored
url = (
    'https://storage.googleapis.com/esmartdata-courses-files/'
    'ds-bootcamp/london_bike.csv'
)

# Read the CSV data from the URL into a pandas DataFrame
df = pd.read_csv(url)

# Convert the 'timestamp' column to datetime format for time-based analysis
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extract the hour component from the 'timestamp' column and create a new 'hour' column
df['hour'] = df['timestamp'].dt.hour

# Extract the month component from the 'timestamp' column and create a new 'month' column
df['month'] = df['timestamp'].dt.month

# Print the first few rows (head) of the DataFrame to get a quick overview
print(df.head())