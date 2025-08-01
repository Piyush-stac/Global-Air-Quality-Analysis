import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Extracting the data from the dataset(csv file)
data = pd.read_csv('global_air_quality_dataset.csv')

#Converting Date column into datetime format
data['Date']= pd.to_datetime(data['Date'])

#Checking for missing/null values
print(f"The number of NAN values in each column : \n{data.isna().sum()}")
print('\n')

# Checking for data types
print(f"The data of each column : \n{data.dtypes}")
print('\n')

# Renaming the columns for ease
data.rename(columns={'PM2.5 (µg/m³)' : 'PM2.5' , 'PM10 (µg/m³)' : 'PM10' , 'NO2 (ppb)' : 'NO2' , 'SO2 (ppb)' : 'SO2' , 'CO (ppm)' : 'CO' , 'O3 (ppb)' : 'O3'} , inplace=True)

# Dropping NAN values if present any
data.dropna(subset=['PM2.5' , 'PM10', 'NO2' , 'SO2', 'CO', 'O3'] , how='any',inplace=True)

# General Overview :
# Number of unique Cities and Countries
cities=data.groupby('City')['City'].count()
print(f"The number of unique cities are :{cities.count()}")
countries=data.groupby('Country')['Country'].count()
print(f"The number of unique cities are :{countries.count()}")
