import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('global_air_quality_dataset.csv')
data.rename(columns={'PM2.5 (µg/m³)' : 'PM2.5' , 'PM10 (µg/m³)' : 'PM10' , 'NO2 (ppb)' : 'NO2' , 'SO2 (ppb)' : 'SO2' , 'CO (ppm)' : 'CO' , 'O3 (ppb)' : 'O3'} , inplace=True)

# AQI Distrbution Over Countries
Country_distribution = data.groupby('Country')['AQI'].mean()
y=Country_distribution.values
x=list(Country_distribution.index)
plt.bar(x,y,label="AQI",color="Green")
plt.xlabel("Countries")
plt.ylabel("AQI")
plt.title("AQI Distribution Over Countries")
plt.tight_layout()
plt.show()
