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

# Pollutant Analysis over Countries
fig ,axs = plt.subplots(2,3,figsize=(5,5))
Country_distribution = data.groupby('Country')[['PM2.5' , 'PM10', 'NO2' , 'SO2', 'CO', 'O3']].mean()

# PM2.5 Distribution
y=Country_distribution['PM2.5'].values
axs[0][0].bar(x,y,color='green',edgecolor='black')
axs[0][0].set_xlabel('Countries')
axs[0][0].set_ylabel('PM2.5 (µg/m³)')
axs[0][0].set_title("PM2.5 (µg/m³) Distribution")

# PM10 Distribution
y=Country_distribution['PM10'].values
axs[0][1].bar(x,y,color='green',edgecolor='black')
axs[0][1].set_xlabel('Countries')
axs[0][1].set_ylabel('PM10 (µg/m³)')
axs[0][1].set_title("PM10 (µg/m³) Distribution")

# NO2 Distribution
y=Country_distribution['NO2'].values
axs[0][2].bar(x,y,color='green',edgecolor='black')
axs[0][2].set_xlabel('Countries')
axs[0][2].set_ylabel('NO2 (ppb)')
axs[0][2].set_title("NO2 (ppb) Distribution")

# SO2 Distribution
y=Country_distribution['SO2'].values
axs[1][0].bar(x,y,color='green',edgecolor='black')
axs[1][0].set_xlabel('Countries')
axs[1][0].set_ylabel('SO2 (ppb)')
axs[1][0].set_title("SO2 (ppb) Distribution")

# CO Distribution
y=Country_distribution['CO'].values
axs[1][1].bar(x,y,color='green',edgecolor='black')
axs[1][1].set_xlabel('Countries')
axs[1][1].set_ylabel('CO (ppm)')
axs[1][1].set_title("CO (ppm) Distribution")

# O3 Distribution
y=Country_distribution['O3'].values
axs[1][2].bar(x,y,color='green',edgecolor='black')
axs[1][2].set_xlabel('Countries')
axs[1][2].set_ylabel('O3 (ppb)')
axs[1][2].set_title("O3 (ppb) Distribution")
plt.tight_layout()
plt.show()


# Polluted Cities
polluted_cities = data.groupby('City')['AQI'].mean()
polluted_cities.sort_values(ascending=False,inplace=True)
print(f"Top 5 most polluted Cities :\n{tuple(polluted_cities.head().index)}")

# AQI Trends with City
AQI_with_City = data.groupby('City')['AQI'].mean()
x=list(AQI_with_City.index)
y=AQI_with_City.values
plt.plot(x,y,marker='o',color='Red',linestyle='--')
plt.xlabel('Cities')
plt.ylabel('AQI')
plt.title("AQI Trends With City")
plt.grid()
plt.show()

# Seasonal Variation Of Pollutants 
data['Month'] = pd.to_datetime(data['Date']).dt.month_name()
pollutant_with_time = data.groupby('Month')[['PM2.5' , 'PM10', 'NO2' , 'SO2', 'CO', 'O3']].mean()
pollutant_with_time = pollutant_with_time.reindex(['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December'])
y=pollutant_with_time.values
x=list(pollutant_with_time.index)
plt.plot(x,y,label=['PM2.5' , 'PM10', 'NO2' , 'SO2', 'CO', 'O3'],marker='o',linestyle='--')
plt.xlabel('Months')
plt.ylabel('Pollutant Level')
plt.title("Seasonal Variation Of Pollutants")
plt.legend()
plt.grid()
plt.show()

# Monthly trend of AQI in top Polluted Cities
AQI_with_time= data.groupby(['City','Month'])['AQI'].mean()
AQI_with_time = AQI_with_time.unstack()
x=list(AQI_with_time.loc['Delhi',:].index)
y=AQI_with_time.loc['Delhi',:].values
plt.plot(x,y,marker='o',color='black',linestyle='--')
plt.xlabel('Months')
plt.ylabel('AQI')
plt.title("Monthly trend of AQI in top Polluted City(Delhi)")
plt.grid()
plt.show()


# Wind Speed vs PM2.5
group=data.groupby('City')['Wind Speed (m/s)'].mean()
x=list(group.index)
y=group.values
plt.scatter(x,y,marker='o',linestyle='--',label='Wind Speed (m/s)'),
plt.xlabel('Cities')
plt.title("Monthly trend of AQI in top Polluted City(Delhi)")
plt.legend()

group=data.groupby('City')['PM2.5'].mean()
x=list(group.index)
y=group.values
plt.scatter(x,y,marker='o',linestyle='--',label='PM2.5'),
plt.xlabel('Cities')
plt.legend()

plt.ylabel('PM2.5 and Wind Speed (m/s)')
plt.title("Wind Speed vs PM2.5")
plt.grid()
plt.show()

