'''
Exercise 178
The df DataFrame is given below. Group this DataFrame by month and calculate the average value for the hum column. Assign the result to humidity_by_month variable and reset the index.

In response, print humidity_by_month DataFrame to the console as shown below. '''

# Import the pandas library for data analysis
import pandas as pd

# Set pandas display options for better readability:
#  - max_columns limits the number of columns shown at once
#  - display.width controls the overall output width
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
# This allows us to extract meaningful date components like month
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extract the month component from the 'timestamp' column
# and create a new column named 'month' for easier analysis
df['month'] = df['timestamp'].dt.month

# Group the DataFrame by the 'month' column
# This allows us to calculate statistics for each month separately
humidity_by_month = df.groupby('month')

# Calculate the average humidity for each month group
# We assume the 'hum' column represents humidity data
humidity_by_month = humidity_by_month['hum'].mean()

# Reset the index to convert the grouped result back into a DataFrame
# with month as a regular column and average humidity as the value
humidity_by_month = humidity_by_month.reset_index()

# Print the DataFrame showing average humidity by month
print(humidity_by_month)

# This code effectively calculates the average humidity for each month 
# in the London bike data. You can use this information to explore 
# potential seasonal trends in humidity and its relationship with bike usage.